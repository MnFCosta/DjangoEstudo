from django.urls import path
from recipes import views


app_name = 'recipes'

urlpatterns = [
    path('', views.view, name="home"),
    path('teste/', views.teste, name="teste"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
    path('recipes/category/<int:category_id>/', views.category, name="category"),
    path('reset/', views.reset, name="reset"),
    path('-/', views.diminui, name="diminuir"),
    path('+/', views.aumento, name="aumentar"),
    path('foto/', views.screenshot, name="foto"),
]