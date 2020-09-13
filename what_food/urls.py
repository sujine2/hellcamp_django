from django.urls import path
from . import views
"""path 장고 함수/ views요소 가져오기"""

urlpatterns = [
    path('', views.index, name='index'),
    path('<country>/', views.food_viewer, name='food_viewer'),
]

