from django.urls import path
from .views import register, confirm_email, login, logout_view

app_name = 'authe'

urlpatterns = [
    path('register/', register, name = 'register'),
    path('confirm/<str:code>', confirm_email, name = 'confirm'),
    path('login/', login, name = 'login'),
    path('logout', logout_view, name='logout'),
]