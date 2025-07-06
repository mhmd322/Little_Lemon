from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet, index, MenuItemViewSet # استيراد مباشر لكل شيء
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
# إعداد الراوتر
router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'booking', BookingViewSet)
router.register(r'menuitem', MenuItemViewSet)


# دمج الروابط
urlpatterns = [
    path('', index, name='home'),          # الصفحة الرئيسية
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
        # روابط API تلقائية
]
