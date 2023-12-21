from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views import generic, View
from django.views.generic.list import MultipleObjectMixin

from backlog.forms import (
    GameSearchForm,
    GamerSearchForm,
    GamerCreationForm,
    GameCreationForm, DeveloperSearchForm
)
from backlog.models import (
    Developer,
    Game,
    Gamer,
    Genre
)


class IndexView(View):
    template_name = 'backlog/index.html'

    def get(self, request, *args, **kwargs):
        num_gamers = Gamer.objects.count()
        num_games = Game.objects.count()
        num_developers = Developer.objects.count()

        num_visits = request.session.get("num_visits", 0)
        request.session["num_visits"] = num_visits + 1

        context = {
            "num_gamers": num_gamers,
            "num_games": num_games,
            "num_developers": num_developers,
            "num_visits": num_visits + 1,
        }

        return render(request, self.template_name, context=context)


class TopGameView(View):
    template_name = 'backlog/top_games.html'

    def get(self, request, *args, **kwargs):
        top_10_games = Game.objects.order_by("-meta_score")[:10]
        context = {"top_10_games": top_10_games}
        return render(request, self.template_name, context=context)


class ToggleGameBacklog(View):
    def get(self, request, pk):
        gamer = request.user
        game = get_object_or_404(Game, id=pk)
        if game in gamer.games.all():
            gamer.games.remove(game)
        else:
            gamer.games.add(
                game,
                through_defaults={
                    "added_to_backlog_at": timezone.now()
                }
            )
            game.added_to_backlog_at = timezone.now()
            game.save()

        return redirect(request.META.get(
            "HTTP_REFERER",
            reverse(
                "backlog:game-detail",
                args=[pk]
            )
        )
        )

    def post(self, request, pk):
        return redirect(request.META.get(
            "HTTP_REFERER",
            reverse(
                "backlog:game-detail",
                args=[pk]
            )
        )
        )


# @login_required
# def toggle_game_backlog(request, pk):
#     gamer = request.user
#     game = get_object_or_404(Game, id=pk)
#     if game in gamer.games.all():
#         gamer.games.remove(game)
#     else:
#         gamer.games.add(
#             game,
#             through_defaults={'added_to_backlog_at': timezone.now()}
#         )
#         game.added_to_backlog_at = timezone.now()
#         game.save()
#
#     return redirect(request.META.get(
#         'HTTP_REFERER',
#         reverse(
#             'backlog:game-detail',
#             args=[pk])
#     )
#     )


class GameListView(generic.ListView):
    model = Game
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GameListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = GameSearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        queryset = Game.objects.all()
        form = GameSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(title__icontains=form.cleaned_data["title"])
        return self.queryset


class GameDetailView(LoginRequiredMixin, generic.DetailView):
    model = Game


class DeveloperListView(generic.ListView):
    model = Developer
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DeveloperListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DeveloperSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Developer.objects.exclude(id=1)
        form = DeveloperSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return self.queryset    


class DeveloperDetailView(
    LoginRequiredMixin,
    generic.DetailView,
    MultipleObjectMixin
):
    model = Developer
    paginate_by = 10

    def get_context_data(self, **kwargs):
        object_list = Game.objects.filter(developers=self.get_object())
        context = super(DeveloperDetailView, self).get_context_data(
            object_list=object_list, **kwargs
        )
        return context


class DeveloperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Developer
    fields = "__all__"
    success_url = reverse_lazy("backlog:developer-list")


class DeveloperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Developer
    fields = "__all__"
    success_url = reverse_lazy("backlog:developer-list")


class DeveloperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Developer
    success_url = reverse_lazy("backlog:developer-list")


class GenreListView(generic.ListView):
    model = Genre
    paginate_by = 10


class GenreDetailView(
    LoginRequiredMixin,
    generic.DetailView,
    MultipleObjectMixin
):
    model = Genre
    paginate_by = 10

    def get_context_data(self, **kwargs):
        object_list = Game.objects.filter(genre=self.get_object())

        search_form = GameSearchForm(self.request.GET)
        if search_form.is_valid():
            title = search_form.cleaned_data.get('title')
            if title:
                object_list = object_list.filter(title__icontains=title)

        context = super(GenreDetailView, self).get_context_data(
            object_list=object_list, **kwargs
        )
        context['search_form'] = search_form
        return context


class GamerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Gamer


class GamerListView(LoginRequiredMixin, generic.ListView):
    model = Gamer
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GamerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = GamerSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = get_user_model().objects.all()
        form = GamerSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return self.queryset


class GamerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Gamer
    form_class = GamerCreationForm


class GamerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Gamer
    success_url = reverse_lazy("backlog:gamer-list")


class GameCreateView(LoginRequiredMixin, generic.CreateView):
    model = Game
    form_class = GameCreationForm
    success_url = reverse_lazy("backlog:game-list")

    def form_valid(self, form):
        developer_names = form.cleaned_data.get('developers', '').split(',')
        developers = [
            Developer.objects.get_or_create(name=name.strip())[0]
            for name in developer_names if name.strip()
        ]
        form.instance.save()
        form.instance.developers.set(developers)
        return super().form_valid(form)


class GameUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Game
    fields = ["title", "developers", "release_date", "genre"]
    success_url = reverse_lazy("backlog:game-list")


class GameDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Game
    success_url = reverse_lazy("backlog:game-list")
