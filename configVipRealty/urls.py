from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, include

from apps.users.views import SignUpView, landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing'),
    path('rent/', include('apps.rent.urls', namespace='rent')),
    path('branch/', include('apps.branch.urls', namespace='branch')),

    path('signup', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
