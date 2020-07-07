from django.urls import path
from . import views

app_name = "team"

urlpatterns = [
    path('', views.view, name='view'),
    path('edit/', views.edit, name='edit'),
]