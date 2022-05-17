from typing import Tuple

from django.contrib import admin

from .models import URLShort


@admin.register(URLShort)
class URLShortAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "url",
        "short_url",
        "created",
        "updated",
        "archived",
    )
    inlines: Tuple = tuple(admin.ModelAdmin.inlines)
    readonly_fields: Tuple = admin.ModelAdmin.readonly_fields + (
        "id",
        "created",
        "updated",
        "archived",
    )
