from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('categories/', categories, name='categories'),
    path('search', data_visualization, name='search'),
]
