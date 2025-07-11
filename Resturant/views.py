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


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking, Menu
from .forms import BookingForm


def home(request):
    return render(request, 'home.html')

def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

@login_required
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'تم الحجز بنجاح ✅')
            return redirect('reversing')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

@login_required
def reversing(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'reversing.html', {'bookings': bookings})

@login_required
def delete_booking(request, booking_id):
    if request.method == 'POST':
        booking = Booking.objects.filter(id=booking_id, user=request.user).first()
        if booking:
            booking.delete()
            messages.success(request, 'تم حذف الحجز بنجاح 🗑️')
        else:
            messages.error(request, 'الحجز غير موجود أو غير مصرح لك بحذفه')
    return redirect('reversing')