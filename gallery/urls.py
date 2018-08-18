from django.urls import path

from . import views

urlpatterns = [  
    path('all/', views.all_gallery, name='all-gallery'),
    path('upload/', views.upload, name='upload'),
    path('view/<uuid>/', views.all_gallery, name='all-gallery'),
]
