from django.urls import path
from . import views

app_name = "player"

urlpatterns = [
    path('', views.view, name='view'),
]