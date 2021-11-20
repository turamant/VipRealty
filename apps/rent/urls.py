from django.urls import path

from apps.rent.views import listview_realty, detail_real, listview_leases, detail_lease, main_rent

app_name = 'rent'

urlpatterns = [
    path('', main_rent, name='main_rent'),
    path('realty/', listview_realty, name='list_realty'),
    path('realty/<int:id>/', detail_real, name='detail_real'),

    path('leases/', listview_leases, name='list_leases'),
    path('leases/<int:pk>/', detail_lease, name='detail_lease'),
]