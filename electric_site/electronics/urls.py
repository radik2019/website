from django.urls import path

from .views import *

urlpatterns = [
    
    path('', home, name='home'),
    path('deletedata/<int:article_id>/', delete_data),
    path('categories/', categories, name='categories'),
    path('search/', data_visualization, name='search'),
    path('search/<int:article_id>/', detailed_data),
    path('search/<int:article_id>/update/', update_data),
    path('search/<int:article_id>/update/updated/', updated),
    path('all_article/', show_all_article, name='all_article'),
    path('all_article/<int:article_id>/', detailed_data, name='dettailed'),
    path('all_article/<int:article_id>/update/', update_data),
    path('all_article/<int:article_id>/update/updated/', updated),
    path('json_data/all/', SerData().all_data),
    path('json_data/searchbrand/<str:brand_name_product>/', SerData().searche_by_brand),
    path('json_data/update-article/', SerData().update_article),
    path('json_data/post/', SerData().post_),
]
