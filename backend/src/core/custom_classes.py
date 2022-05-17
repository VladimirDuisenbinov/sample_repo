from django.db import models
from django.db.models import Manager


class BaseModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True, help_text="created", verbose_name="created"
    )
    updated = models.DateTimeField(
        auto_now=True, help_text="updated", verbose_name="updated"
    )
    archived = models.BooleanField(
        default=False, help_text="archived", verbose_name="archived"
    )
    objects: Manager

    class Meta:
        abstract = True
