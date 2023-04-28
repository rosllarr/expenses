from django.urls import path

from . import views

app_name = 'monthly'
urlpatterns = [
    path('', views.index, name='index')
]
