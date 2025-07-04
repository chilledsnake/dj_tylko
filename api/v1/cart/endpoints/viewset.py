from rest_framework import viewsets

from api.v1.cart.serializers import CartSerializer
from modules.cart.models import Cart


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
