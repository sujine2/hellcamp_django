from django.urls import path
from . import views
"""path 장고 함수/ views요소 가져오기"""

urlpatterns = [
    path('', views.index, name='index'),
    path('w/', views.w, name='w_food'),
    path('k/', views.k, name='w_food'),
    path('j/', views.j, name='w_food'),
    path('c/', views.c, name='w_food'),
]