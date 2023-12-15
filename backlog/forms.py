from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from backlog.models import Game, Developer, Gamer


class GameSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search game by title..."
            }
        )
    )


class GamerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search user..."
            }
        )
    )


class DeveloperSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search developer by name..."
            }
        )
    )


class GamerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Gamer
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
        )

