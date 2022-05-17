from django.db import models
from django.db.models import Manager

from core.custom_classes import BaseModel

from .services import get_short_url


class URLShort(BaseModel):
    url = models.URLField(
        verbose_name="url", help_text="url",
        null=False, blank=False,
    )
    short_url = models.CharField(
        verbose_name="short_url", help_text="short_url",
        null=False, blank=False,
        max_length=15
    )
    objects: Manager

    class Meta:
        app_label = "url_short"
        db_table = "url_short.url_shorts"
        verbose_name = "url_short"
        verbose_name_plural = "url_shorts"

    def save(self, *args, **kwargs):
        if not self.short_url:
            short_url = get_short_url()
            objs = URLShort.objects.filter(short_url=short_url)

            while len(objs) > 0:
                short_url = get_short_url()
                objs = URLShort.objects.filter(short_url=short_url)
            
            self.short_url = short_url

        return super().save(*args, **kwargs)
