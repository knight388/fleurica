from django.urls import path

from . import views

urlpatterns = [
	path('shop/', views.bouquet_shop, name='bouquet-shop'),

    path('bouquets/all/', views.all_products, name='all-bouquets'),
    path('bouquets/new/', views.edit_bouquet, name='new-bouquet'),
    path('bouquets/edit/<uuid>/', views.edit_bouquet, name='edit-bouquet'),
    path('bouquets/view/<slug>-<bid>/', views.view_bouquet, name='view-bouquet'),

    path('ajax/load-bouquet/', views.ajax_load_bouquets, name='ajax-load-bouquets'),
    path('ajax/manage-cart/', views.ajax_manage_cart, name='ajax-manage-cart'),
]
