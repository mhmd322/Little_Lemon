from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet, MenuItemViewSet
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# إعداد الراوتر
router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'booking', BookingViewSet)
router.register(r'menuitem', MenuItemViewSet)

urlpatterns = [
    path('', views.home, name='home'),          # الصفحة الرئيسية
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('', include('accounts.urls')),
    path('menu/', views.menu, name='menu'),
    path('booking/', views.booking, name='booking'),
    path('reversing/', views.reversing, name='reversing'),
    path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]
