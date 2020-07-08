from django.urls import path
from . import views

app_name = "profile"

urlpatterns = [
    path('', views.red, name='redirect'),
    path('<int:profile_id>/', views.view, name='view'),
    path('create/', views.create, name="create"),
    path('edit/', views.edit, name="edit"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
]