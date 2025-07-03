from rest_framework import viewsets

from modules.shelf.models import Shelf


class ShelfViewSet(viewsets.ModelViewSet):
    queryset = Shelf.objects.all()
