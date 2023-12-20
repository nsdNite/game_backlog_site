from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from backlog.models import Gamer, Game, Developer, Genre, Category


@admin.register(Gamer)
class GamerAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                    )
                },
            ),
        )
    )


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("genre",)


admin.site.register(Developer)
admin.site.register(Genre)
admin.site.register(Category)
