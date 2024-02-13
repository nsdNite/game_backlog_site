from django import forms
from django.contrib.auth.forms import UserCreationForm

from backlog.models import Game, Gamer


class GameSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search game by title..."}
        ),
    )


class GamerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Search user..."}),
    )


class DeveloperSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search developer by name..."}
        ),
    )


class GamerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Gamer
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
        )


class GameCreationForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["title", "release_date", "genre"]

    developers = forms.CharField(max_length=100)
    release_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
