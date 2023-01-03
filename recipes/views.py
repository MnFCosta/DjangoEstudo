from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def view(request):
    return render(request, 'recipes/home.html', context={
        "name": 'Manoel Costa'
    })


def teste(request):
    return render(request, 'teste/teste.html')

 
