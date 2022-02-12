from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('categories/', categories, name='categories'),
    path('search', data_visualization, name='search'),
    path('all_article/', show_all_article, name='all_article'),
    path('all_article/<int:article_id>', detailed_data, name='dettailed')
]
