from rest_framework import serializers

from modules.shelf.models import Shelf


class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = "__all__"
