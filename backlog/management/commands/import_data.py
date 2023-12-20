import json

from django.core.management.base import BaseCommand

from backlog.models import Category, Developer, Game, Genre


class Command(BaseCommand):
    help = "Retrieves data from steamdb.json file"

    def handle(self, *args, **options):
        json_path = "steamdb.json"

        fields_to_load = [
            "published_meta",
            "image",
            "name",
            "description",
            "developers",
            "categories",
            "genres",
            "meta_score",
        ]

        Developer.objects.get_or_create(
            name="Unknown"
        )

        with open(json_path, "r", encoding='ISO-8859-1') as json_file:
            json_data = json.load(json_file)
            counter = 0

        for game_data in json_data[:1000]:
            filtered_data = {
                key: game_data.get(key)
                for key in fields_to_load if key in game_data
            }
            developers_name = filtered_data.get("developers")
            category_names = filtered_data.get("categories")
            genre_names = filtered_data.get("genres")

            # Creating developers
            if developers_name:
                developers_names = (str(developers_name).split(","))
                developers = [
                    Developer.objects.get_or_create(
                        name=developer.strip())[0]
                    for developer in developers_names
                ]
            else:
                unknown_developer, created = Developer.objects.get_or_create(
                    name="Unknown"
                )
                developers = [unknown_developer]

            # Creating genres
            if genre_names:
                genre_names = filtered_data.get("genres", "").split(",")
                genres = [
                    Genre.objects.get_or_create(
                        name=genre.strip())[0]
                    for genre in genre_names
                ]

            # Creating categories
            if category_names:
                category_names = category_names.split(",")
                categories = [
                    Category.objects.get_or_create(
                        name=category.strip())[0]
                    for category in category_names
                ]

            # Creating game
            game_title = filtered_data.get("name")
            existing_game = Game.objects.filter(title=game_title).first()

            if existing_game:
                print(f"Skipping existing game: {game_title}")
                counter += 1
            else:
                new_game = Game.objects.create(
                    title=filtered_data.get("name"),
                    description=filtered_data.get("description"),
                    meta_score=filtered_data.get("meta_score"),
                    release_date=filtered_data.get("published_meta"),
                    image_url=filtered_data.get("image")
                )
                new_game.developers.set(developers)
                new_game.genre.set(genres)
                new_game.category.set(categories)
                counter += 1
                print(f"Loaded {counter} of {len(json_data)}.")

        print(f"Finished loading {counter} objects.")
