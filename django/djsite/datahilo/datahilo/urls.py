from django.contrib import admin
from datahilo import settings
from django.conf.urls.static import static
from core.views import *
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
