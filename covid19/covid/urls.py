from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Home, DashBoard

urlpatterns = [
    path('', Home, name='home-page'),
    path('dashboard/', DashBoard, name='dashboard'),
]
