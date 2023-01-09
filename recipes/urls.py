from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.view),
    path('recipes/<int:id>/', views.recipe),
]