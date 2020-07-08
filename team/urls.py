from django.urls import path
from . import views

app_name = "team"

urlpatterns = [
    path('<int:team_id>/', views.view, name='view'),
    path('<int:team_id>/edit/', views.edit, name='edit'),
]