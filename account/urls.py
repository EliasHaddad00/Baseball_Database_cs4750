from django.urls import path
from . import views

app_name = "profile"

urlpatterns = [
    path('', views.view, name='view'),
    path('create/', views.create, name="create"),
    path('login/', views.login, name="login")
]