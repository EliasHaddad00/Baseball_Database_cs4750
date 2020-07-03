from django.urls import path
from . import views

app_name = "team"

urlpatterns = [
    path('', views.view, name='view'),
    path('editTeam/', views.editTeamView.as_view(), name='editTeam'),
    path('teamInfo/', views.teamInfoView.as_view(), name='teamInfo'),
]