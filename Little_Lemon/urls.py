from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Resturant.urls')),         # للصفحة الرئيسية أو واجهة الموقع
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('accounts/', include('accounts.urls')),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
