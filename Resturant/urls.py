from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet, index  # استيراد مباشر لكل شيء

# إعداد الراوتر
router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'booking', BookingViewSet)

# دمج الروابط
urlpatterns = [
    path('', index, name='home'),          # الصفحة الرئيسية
    path('api/', include(router.urls)),    # روابط API تلقائية
]
