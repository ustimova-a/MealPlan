from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Product
import random
from .parser import parse


def index(request):
    meat = Product.objects.filter(type__name="Meat")
    sides = Product.objects.filter(type__name='Sides')
    random_meat = random.choice(meat)
    random_sides = random.choice(sides)
    return render(request, 'products/index.html', {'random_meat': random_meat, 'random_sides': random_sides})


def details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    URL_TEMPLATE = f"https://eda.ru/recepty/ingredienty/{product.eda_id}"
    parse_list = parse(url=URL_TEMPLATE)
    recipe_name = [item['name'] for item in parse_list]
    recipe_preptime = [item['prep_time'] for item in parse_list]
    return render(request, 'products/details.html', {'product': product, 'parse_list': parse_list, 'recipe_name': recipe_name, 'recipe_preptime': recipe_preptime})
