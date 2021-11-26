from django.urls import path

from apps.rent.views import listview_leases, detail_lease, main_rent, listview_realties, \
    detail_realty, create_lease

app_name = 'rent'

urlpatterns = [
    path('', main_rent, name='main_rent'),
    path('realties/', listview_realties, name='list_realties'),
    path('realties/<int:id>/', detail_realty, name='detail_realty'),

    path('leases/create/', create_lease, name='create_lease'),
    path('leases/', listview_leases, name='list_leases'),
    path('leases/<int:pk>/', detail_lease, name='detail_lease'),
]