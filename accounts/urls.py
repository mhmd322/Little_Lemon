from django.urls import path
from .views import CustomLoginView, SafeLogoutView, RegisterView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', SafeLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]