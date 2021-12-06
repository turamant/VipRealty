from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('branchs/', include('apps.branch.urls', namespace='branch')),
    path('', include('apps.core.urls', namespace='core')),
    path('', include('apps.rent.urls', namespace='rent')),

    #path('signup', SignUpView.as_view(), name='signup'),
    #path('login/', LoginView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



