from rest_framework import viewsets

from api.v1.order.serializers import OrderSerializer
from modules.order.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
