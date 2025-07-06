from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from rest_framework import viewsets
from .models import Menu, Booking,MenuItem
from .serializers import MenuSerializer, BookingSerializer,MenuItemSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset= MenuItem.objects.all()
    serializer_class= MenuItemSerializer


def index(request):
    return render(request, 'index.html', {
        'current_year': datetime.now().year
    })
