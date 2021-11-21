from django.urls import path

from apps.rent.views import listview_leases, detail_lease, main_rent, listview_property, \
    detail_property

app_name = 'rent'

urlpatterns = [
    path('', main_rent, name='main_rent'),
    path('realty/', listview_property, name='list_property'),
    path('realty/<int:id>/', detail_property, name='detail_property'),

    path('leases/', listview_leases, name='list_leases'),
    path('leases/<int:pk>/', detail_lease, name='detail_lease'),
]