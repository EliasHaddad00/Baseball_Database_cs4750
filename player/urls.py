from django.urls import path
from . import views

app_name = "player"

urlpatterns = [
    path('<int:player_id>', views.view, name='view'),
    path('<int:player_id>/edit/', views.edit, name='edit'),
    path('<int:player_id>/delete/', views.delete, name='delete'),
    path('new/', views.create, name='create')
]