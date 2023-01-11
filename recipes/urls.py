from django.urls import path
from recipes import views


app_name = 'recipes'

urlpatterns = [
    path('', views.view, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]