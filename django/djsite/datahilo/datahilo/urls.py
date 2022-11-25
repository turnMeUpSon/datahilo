from django.contrib import admin
from django.urls import path

from core.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
]