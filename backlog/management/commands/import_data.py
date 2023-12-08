import json

from backlog.models import Category, Developer, Game, Genre

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

with open(json_path, "r") as json_file:
    json_data = json.load(json_file)
    filtered_data = {
        key: json_data[key] for key in fields_to_load if key in json_data
    }

for game in filtered_data:
    # Creating developers
    developer_name = filtered_data.get("developers")
    developer, created = Developer.objects.create(name=developer_name)

    # Creating genres
    genre_names = filtered_data.get("genres", "").split(",")
    genres = [
        Genre.objects.get_or_create(name=genre.strip())[0] for genre in genre_names
    ]

    # Creating categories
    category_names = filtered_data.get("categories", "").split(",")
    categories = [
        Category.objects.get_or_create(name=category.strip())[0] for category in category_names
    ]

    # Creating game
    new_game = Game.objects.create(
        title=filtered_data.get("name"),
        description=filtered_data.get("description"),
        developer=developer,
        meta_score=filtered_data.get("meta_score"),
        release_date=filtered_data.get("published_meta"),
        image_url=filtered_data.get("image")
    )
    new_game.genre.set(genres)
    new_game.category.set(categories)
