from django.urls import path

from . import views

urlpatterns = [
    path('view/', views.shop, name='view-shop'),
]
