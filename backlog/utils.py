import requests
from io import BytesIO
from django.core.files import File
from PIL import Image

from backlog.models import Game


def fetch_and_save_image(game: Game):
    response = requests.get(game.image_url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image_io = BytesIO()
        image.save(image_io, format="JPEG")
        game.image.save(f"{Game.title}_img.jpg", File(image_io), save=False)
        game.save()
