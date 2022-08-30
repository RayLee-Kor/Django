from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.hello),
    path('jwt/',views.jwtfuc),
    path('get_data',views.get_data)
]