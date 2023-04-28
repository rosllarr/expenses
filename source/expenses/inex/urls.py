from django.urls import path

from . import views

app_name = 'inex'
urlpatterns = [
    path('', views.index, name='index')
]
