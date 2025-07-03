from rest_framework import viewsets

from modules.order.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
