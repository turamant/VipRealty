from django.urls import path
from django.contrib.auth import views as auth_views

from apps.branch.views import listview_staff, detail_staff, listview_salary_staff,\
    become_branch, branch_admin, add_realty, edit_realty, delete_realty,\
    branch_detail, branch_list

app_name = 'branch'

urlpatterns = [
    path('become-client/', become_client, name='become_client'),
    path('client-admin/', client_admin, name='client_admin'),

    path('add-realty/', add_realty, name='add_realty'),
    path('update/<slug:category_slug>/<slug:slug>/', edit_realty, name='edit_realty'),
    path('delete/<slug:category_slug>/<slug:slug>/', delete_realty, name='delete_realty'),

    path('staff/', listview_staff, name='list_staff'),
    path('staff/salary/', listview_salary_staff, name='salary_staff'),
    path('staff/<int:pk>/', detail_staff, name='detail_staff'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='branch/login.html'), name='login'),

    path('', branch_list, name='branch_list'),
    path('<int:pk>/', branch_detail, name='branch_detail'),
]