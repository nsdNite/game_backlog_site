from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from backlog.models import Game, Developer, Gamer

GAME_URL = reverse("backlog:game-list")
GAMER_URL = reverse("backlog:gamer-list")
DEVELOPER_URL = reverse("backlog:developer-list")


class PublicListTest(TestCase):
    def setUp(self):
        self.gamer = Gamer.objects.create_user(
            username="test_gamer",
            password="test_password"
        )
        self.developer = Developer.objects.create(name="test_dev")
        self.game = Game.objects.create(
            title="Test_game"
        )
        self.game.developers.set([self.developer])

    def test_game_detail_login_required(self):
        result = self.client.get(reverse(
            "backlog:game-detail",
            kwargs={'pk': self.game.pk}
        )
        )
        self.assertNotEqual(result.status_code, 200)

    def test_developer_detail_login_required(self):
        result = self.client.get(reverse(
            "backlog:developer-detail",
            kwargs={'pk': self.developer.pk}
        )
        )
        self.assertNotEqual(result.status_code, 200)

    def test_gamer_detail_login_required(self):
        result = self.client.get(reverse(
            "backlog:gamer-detail",
            kwargs={'pk': self.gamer.pk}
        )
        )
        self.assertNotEqual(result.status_code, 200)


class PrivateListTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test0451"
        )
        self.client.force_login(self.user)

    def test_retrieve_game_list(self):
        developer = Developer.objects.create(
            name="test_dev",
        )
        game_one = Game.objects.create(title="test_01",)
        game_one.developers.set([developer])
        game_two = Game.objects.create(title="test_02")
        game_two.developers.set([developer])
        response = self.client.get(GAME_URL)
        self.assertEqual(response.status_code, 200)
        games = Game.objects.all()
        self.assertEqual(
            list(response.context["game_list"]),
            list(games)
        )

    def test_retrieve_developers_list(self):
        Developer.objects.create(name="Unknown")
        Developer.objects.create(name="test_dev_01")
        Developer.objects.create(name="test_dev_02")
        response = self.client.get(DEVELOPER_URL)
        self.assertEqual(response.status_code, 200)
        developers = Developer.objects.all()
        self.assertEqual(
            list(response.context["developer_list"]),
            list(developers)[1:]
        )

    def test_retrieve_gamer_list(self):
        response = self.client.get(GAMER_URL)
        self.assertEqual(response.status_code, 200)
        gamers = Gamer.objects.all()
        self.assertEqual(
            list(response.context["gamer_list"]),
            list(gamers)
        )
