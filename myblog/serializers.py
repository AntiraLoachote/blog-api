# customers/serializers.py
from rest_framework import serializers

from . import models


class PostSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = models.Post
        fields = '__all__'
