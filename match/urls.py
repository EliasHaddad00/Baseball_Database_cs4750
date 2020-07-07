from django.urls import path
from . import views

app_name = "match"

urlpatterns = [
    path('', views.view, name='view'),
    path('new', views.create, name='create'),
]