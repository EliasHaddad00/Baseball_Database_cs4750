from django.urls import path
from . import views

app_name = "player"

urlpatterns = [
    path('', views.view, name='view'),
    path('edit/', views.edit, name='edit'),
    path('delete/', views.delete, name='delete'),
    path('new/', views.create, name='create')
]