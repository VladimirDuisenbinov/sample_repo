from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .repos import URLShortRepo

from .models import URLShort


class InURLShortSerializer(serializers.ModelSerializer):
    url = serializers.CharField(
        required=True,
        validators=(
            UniqueValidator(
                queryset=URLShortRepo.list()
            ),
        ),
    )
    short_url = serializers.CharField(read_only=True)

    class Meta:
        model = URLShort
        exclude = ('created', 'updated', 'archived')


class OutURLShortSerializer(serializers.ModelSerializer):
    url = serializers.CharField(read_only=True)
    short_url = serializers.CharField(read_only=True)

    class Meta:
        model = URLShort
        exclude = ('created', 'updated', 'archived')
