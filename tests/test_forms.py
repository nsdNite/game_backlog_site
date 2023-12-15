from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from backlog.forms import GamerCreationForm
from backlog.models import Developer, Game, Gamer

GAME_URL = reverse("backlog:game-list")
GAMER_URL = reverse("backlog:gamer-list")
DEVELOPER_URL = reverse("backlog:developer-list")


class FormsTest(TestCase):
    def test_create_user(self):
        form_data = {
            "username": "test_user",
            "password1": "test0451",
            "password2": "test0451",
            "first_name": "Test",
            "last_name": "Gamer",
        }
        form = GamerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class FormSearchTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_gamer",
            password="test0451"
        )
        self.client.force_login(self.user)

    def test_search_game_by_title(self):
        developer = [Developer.objects.create(name="test_dev"),]
        game = Game.objects.create(
            title="test_game",
        )
        game.developers.set(developer)
        searched_title = "test"
        response = self.client.get(GAME_URL, {"title": searched_title})
        self.assertEqual(response.status_code, 200)
        context = Game.objects.filter(title__icontains=searched_title)
        self.assertEqual(list(response.context["game_list"]), list(context))

    def test_search_driver_by_username(self):
        Gamer.objects.create(
            username="test_gamer_02",
            password="test0451",
        )

        searched_name = "test"
        response = self.client.get(GAMER_URL, {"username": searched_name})
        self.assertEqual(response.status_code, 200)
        context = Gamer.objects.filter(username__icontains=searched_name)
        self.assertEqual(list(response.context["gamer_list"]), list(context))

    def test_search_developer_by_name(self):
        # Unknown dev appears at id 1 and is hidden in view
        Developer.objects.create(name="Unknown")
        Developer.objects.create(name="test_dev_02")
        searched_name = "test"
        response = self.client.get(DEVELOPER_URL, name=searched_name)
        self.assertEqual(response.status_code, 200)
        context = Developer.objects.filter(name__icontains=searched_name)
        self.assertEqual(
            list(response.context["developer_list"]),
            list(context)
        )
