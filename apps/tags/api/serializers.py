from rest_framework import serializers

from apps.tags.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [

            'text',

        ]


class TagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
          'text'
        ]
