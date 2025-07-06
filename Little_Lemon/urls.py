from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Resturant.urls')),         # للصفحة الرئيسية أو واجهة الموقع
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
