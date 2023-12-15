from django.urls import path

from .views import (
    index,
    GameDetailView,
    GameListView,
    GameCreateView,
    GameUpdateView,
    GameDeleteView,
    DeveloperListView,
    DeveloperDetailView,
    DeveloperCreateView,
    DeveloperUpdateView,
    DeveloperDeleteView,
    GenreListView,
    GenreDetailView,
    GamerDetailView,
    GamerListView,
    GamerCreateView,
    GamerDeleteView,
    top_game,
    toggle_game_backlog,
)

urlpatterns = [
    path("", index, name="index"),
    path("games/", GameListView.as_view(), name="game-list"),
    path("games/<int:pk>", GameDetailView.as_view(), name="game-detail"),
    path("games/top100/", top_game, name="top_game"),
    path("games/create/", GameCreateView.as_view(), name="game-create"),
    path("games/<int:pk>/update/", GameUpdateView.as_view(), name="game-update"),
    path("games/<int:pk>/delete/", GameDeleteView.as_view(), name="game-delete"),
    path(
        "games/<int:pk>/toggle-backlog/",
        toggle_game_backlog,
        name="toggle-game-backlog",
    ),
    path("developers/", DeveloperListView.as_view(), name="developer-list"),
    path("developers/<int:pk>/", DeveloperDetailView.as_view(), name="developer-detail"),
    path("developers/create/", DeveloperCreateView.as_view(), name="developer-create"),
    path("developers/<int:pk>/update/", DeveloperUpdateView.as_view(), name="developer-update"),
    path("developers/<int:pk>/delete/", DeveloperDeleteView.as_view(), name="developer-delete"),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("gamers/", GamerListView.as_view(), name="gamer-list"),
    path("gamers/<int:pk>/", GamerDetailView.as_view(), name="gamer-detail"),
    path("gamers/create/", GamerCreateView.as_view(), name="gamer-create"),
    path("gamers/<int:pk>/delete/", GamerDeleteView.as_view(), name="gamer-delete"),
]

app_name = "backlog"
