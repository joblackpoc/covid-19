from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home-page'),
    path('dashboard/', DashBoard, name='dashboard-page'),
    path('icons/', Icons, name='icons-page'),
    path('tables/', Tables, name='tables-page'),
    path('user/', User, name='user-page'),
    path('typography/', Typography, name='typography-page'),
    path('notifications/', Notifications, name='notifications-page'),
    path('upgrade/', Upgrade, name='upgrade-page'),
    path('maps/', Maps, name='maps-page'),
    path('rtl/', Rtl, name='rtl-page'),
    
]
