from rest_framework import viewsets

from api.v1.shelf.serializers import ShelfSerializer
from modules.shelf.models import Shelf


class ShelfViewSet(viewsets.ModelViewSet):
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer
