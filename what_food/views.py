from random import randint
from django.shortcuts import render
from .models import Food
# Create your views here.



def index(request):
    return render(request, 'what_food/post_list.html', {})



def w(request):

    foods = Food.objects.filter(country='w')
    foods = foods[randint(0, len(foods) - 1)]

    food = Food.objects.filter(country='w')
    names = []
    urls = []
    for i in food:
        names.append(i.name)
        urls.append(i.picture.url)

    return render(request, 'what_food/w_food.html', {'foods': foods, 'names': names, 'urls': urls })

def k(request):
    foods = Food.objects.filter(country='k')
    foods = foods[randint(0, len(foods) - 1)]

    food = Food.objects.filter(country='k')
    names = []
    urls = []
    for i in food:
        names.append(i.name)
        urls.append(i.picture.url)

    return render(request, 'what_food/w_food.html', {'foods': foods, 'names': names, 'urls': urls})


def j(request):
    foods = Food.objects.filter(country='j')
    foods = foods[randint(0, len(foods) - 1)]

    food = Food.objects.filter(country='j')
    names = []
    urls = []
    for i in food:
        names.append(i.name)
        urls.append(i.picture.url)

    return render(request, 'what_food/w_food.html', {'foods': foods, 'names': names, 'urls': urls})


def c(request):
    foods = Food.objects.filter(country='c')
    foods = foods[randint(0, len(foods) - 1)]

    food = Food.objects.filter(country='c')
    names = []
    urls = []
    for i in food:
        names.append(i.name)
        urls.append(i.picture.url)

    return render(request, 'what_food/w_food.html', {'foods': foods, 'names': names, 'urls': urls})



