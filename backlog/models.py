from django.contrib.auth.models import AbstractUser
from django.db import models


class Developer(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Gamer(AbstractUser):
    class Meta:
        verbose_name = "gamer"
        verbose_name_plural = "gamers"

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=255, unique=False)
    description = models.TextField(blank=True, null=True)
    developers = models.ManyToManyField(
        Developer,
        related_name="games"
    )
    genre = models.ManyToManyField(
        Genre,
        related_name="games"
    )
    category = models.ManyToManyField(
        Category,
        related_name="games"
    )
    meta_score = models.IntegerField(blank=True, null=True)
    gamers = models.ManyToManyField(
        Gamer,
        related_name="games",
    )
    release_date = models.DateField(blank=True, null=True)
    image_url = models.URLField()
    image = models.ImageField(
        blank=True,
        null=True
    )
