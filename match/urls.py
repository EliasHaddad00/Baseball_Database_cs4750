from django.urls import path
from . import views

app_name = "match"

urlpatterns = [
    path('<int:match_id>/', views.view, name='view'),
    path('new/', views.create, name='create'),
    path('<int:match_id>/edit/', views.edit, name='edit'),
    path('<int:match_id>/delete/', views.delete, name="delete"),
]