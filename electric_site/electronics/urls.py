from django.urls import path

from .views import *

urlpatterns = [
    path('', home),
    path('categories/', categories),
    path('search', data_visualization),
]
