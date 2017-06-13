from rest_framework import serializers
from .models import Noticias


class NoticiasSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        model = Noticias
        depth = 1
        fields = ['id', 'title', 'url', 'summary', 'publish', 'status']