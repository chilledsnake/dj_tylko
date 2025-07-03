from rest_framework import viewsets

from modules.cart.models import Cart


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
