from django.shortcuts import render

# Create your views here.


def view(request):
    return render(request, 'recipes/pages/home.html', context={
        "name": 'Manoel Costa'
    })


def teste(request):
    return render(request, 'teste/teste.html')

 
