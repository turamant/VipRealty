from django.urls import path

from apps.branch.views import listview_staff, detail_staff, listview_salary_staff

app_name = 'branch'

urlpatterns = [
    path('staff/', listview_staff, name='list_staff'),
    path('staff/salary/', listview_salary_staff, name='salary_staff'),
    path('staff/<int:pk>/', detail_staff, name='detail_staff'),
]