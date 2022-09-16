from rest_framework import serializers
from .models import Film
from .models import Comments


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        fields = ['title', 'description', 'created_at', 'rate', 'comments', 'user']

