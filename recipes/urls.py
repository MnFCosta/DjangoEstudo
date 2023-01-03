from django.urls import path
from recipes.views import view, teste

urlpatterns = [
    path('', view),
    path('teste/', teste)
]