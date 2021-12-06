from django.urls import path

from apps.rent.views import listview_leases, detail_lease, listview_realties, \
    detail_realty, create_lease, list_clients, detail_client, create_client, category, realty, \
    search

app_name = 'rent'

urlpatterns = [
    path('search/', search, name='search'),
    path('realties/<slug:category_slug>/<slug:realty_slug>/', realty, name='realty'),
    path('realties/<slug:category_slug>/', category, name='category'),




    path('leases/create/', create_lease, name='create_lease'),
    path('leases/', listview_leases, name='list_leases'),
    path('leases/<int:pk>/', detail_lease, name='detail_lease'),

    path('clients/create/', create_client, name='create_client'),
    path('clients/', list_clients, name='list_clients'),
    path('clients/<int:pk>/', detail_client, name='detail_client'),



]