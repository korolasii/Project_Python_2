from django.urls import path

from .views import *

urlpatterns = [
    path('search/', search, name='search'),
    path('<str:slug>/', details, name='details'),
    path('random/', random_article, name='random_article'),
    path('', articles_list, name='blog'),
    path('tag/<str:tag>/', articles_tag_list, name='articles_tag_list'),
    path('category/<str:category>/', articles_category_list, name='articles_category_list'),
]