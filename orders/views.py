from orders.models import Orders
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import OrderSerializer
from . models import Orders
from rest_framework import permissions 
from .permissions import IsOwner



# Create your views here.

class OrderAPIView(ListCreateAPIView):
    serializer_class=OrderSerializer
    queryset=Orders.objects.all()
    permission_classes=(permissions.IsAuthenticated,)


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=OrderSerializer
    queryset=Orders.objects.all()
    permission_classes=(permissions.IsAuthenticated,IsOwner,)
    lookup_field='id'


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)