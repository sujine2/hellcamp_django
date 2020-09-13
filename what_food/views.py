from django.shortcuts import render, redirect

from .models import Food

import random


def index(request):
    return render(request, 'what_food/post_list.html', {})


def food_viewer(request, country):
    foods = Food.objects.filter(country=country)
    names, urls = [], []

    if len(foods) == 0:
        return redirect('/')

    for food in foods:
        names.append(food.name)
        urls.append(food.picture.url)

    food = random.choice(foods)

    return render(request, 'what_food/w_food.html', {'foods': food, 'names': names, 'urls': urls })

