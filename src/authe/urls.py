from django.urls import path
from .views import register, confirm_email

urlpatterns = [
    path('register/', register, name = 'register'),
    path('confirm/<str:code>', confirm_email, name = 'confirm'),
]