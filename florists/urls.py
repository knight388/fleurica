from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.florist_signup, name='florist-signup'),
    path('all/', views.all_florists, name='all-florists'),
    path('signups/', views.all_florists, name='signups-florists'),
    path('edit/<uuid>/', views.edit_florist, name='edit-florist'),
    path('ajax/confirm/', views.ajax_confirm_f, name='ajax-confirm-f'),
]
