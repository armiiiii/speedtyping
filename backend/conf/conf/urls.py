"""conf.urls"""

from django.contrib import admin
from django.urls import path

from .buisneslogic import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/logicendpoint', view), # Buisnesslogic path
]
