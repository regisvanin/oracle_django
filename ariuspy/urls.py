from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls')),
    path('nfce/', include('apps.nfce.urls')),
    path('estform/', include('apps.estform.urls')),
    path('admin/', admin.site.urls),
]
