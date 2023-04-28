from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('inex/', include('inex.urls')),
    path('monthly/', include('monthly.urls')),
    path('admin/', admin.site.urls),
]
