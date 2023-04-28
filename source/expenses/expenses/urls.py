from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('inex/', include('inex.urls')),
    path('admin/', admin.site.urls),
]
