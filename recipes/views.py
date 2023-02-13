from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib import messages
from utils.recipes.factory import make_recipe
from recipes.models import Recipe
from django.http import Http404
from django.shortcuts import redirect

# Create your views here.

i = 0
n1 = 1
n2 = 6

def view(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by("-id")
    
    if recipes: 
        base_template = "global/base.html"
        if len(recipes) == 1:
            messages.success(request, f'{len(recipes)} receita encontradas!')
        else:
            messages.success(request, f'{len(recipes)} receitas encontradas!')
    else:
        base_template = "global/base_contentless.html"
        messages.error(request, 'SEM RECEITAS!')

    return render(request, 'recipes/pages/home.html', context={
        "recipes": recipes,
        "template": base_template,
    })

def teste(request):
    global n1
    global n2
    
    n1 += 5
    n2 += 5

    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by("-id")
    
    if recipes: 
        base_template = "global/base.html"
    else:
        base_template = "global/base_contentless.html"

    iterator = range(n1,n2)


    return render(request, 'recipes/pages/prefeitura.html', context={
        "recipes": recipes,
        "template": base_template,
        'iterator': iterator,
    })
    

def category(request, category_id):
    #Queryset e erro 404 feito sem shortcut
    """ recipes = Recipe.objects.filter(    
        category__id=category_id,
        is_published=True,
        ).order_by("-id")


    if not recipes:

        raise Http404("Página não encontrada :(") """
    
    #QUeryset com shortcut get_list_or_404
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
        ).order_by("-id")
    )


    return render(request, 'recipes/pages/category.html', context={
        "recipes": recipes,
        "title": f'{recipes[0].category.name}',
    })


def recipe(request, id):
    
    recipe = get_object_or_404(Recipe,
        pk=id,
        is_published=True,
    )
    return render(request, 'recipes/pages/recipe-view.html', context={
        "recipe": recipe,
        "is_detail_page": True,
    })

