from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='eauth-login'),
    path('signup/', views.signup, name='eauth-signup'),
]
