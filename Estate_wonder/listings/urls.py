from django.urls import path
from . import views

app_name = 'listing'

urlpatterns = [
    path('<int:listing_id>/', views.listing_detail, name='listing_detail'),
    path('list/', views.listing_list, name='listing_list'),
    path('search/', views.listing_search_results, name='listing_search_results'),
    path('add/', views.listing_form, name='listing_add'),
    path('<int:listing_id>/edit/', views.listing_form, name='listing_edit'),
    path('<int:listing_id>/delete/', views.listing_delete_confirm, name='listing_delete_confirm'),
    path('success/', views.listing_success, name='listing_success'),
    path('error/', views.listing_error, name='listing_error'),
]
