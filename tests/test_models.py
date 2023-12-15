from django.contrib.auth import get_user_model
from django.test import TestCase

from backlog.models import Game, Gamer, Developer


class ModelTests(TestCase):
    def test_developer_str(self):
        developer = Developer.objects.create(
            name="test_dev",
        )
        self.assertEqual(
            str(developer),
            f"{developer.name}"
        )

    def test_game_str(self):
        developer = Developer.objects.create(
            name="test_dev",
        )
        game = Game.objects.create(
            title="test_game",)
        game.developers.set([developer])
        self.assertEqual(str(game), game.title)

    def test_create_driver(self):
        username = "Test_gamer"
        password = "Test0451"
        gamer = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name="Test",
            last_name="Gamer",
        )

        self.assertEqual(gamer.username, username)
        self.assertTrue(gamer.check_password(password))
        self.assertEqual(
            str(gamer),
            f"{gamer.username} ({gamer.first_name} {gamer.last_name})"
        )
