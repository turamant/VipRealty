
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rent/', include('apps.rent.urls', namespace='rent'))
]
