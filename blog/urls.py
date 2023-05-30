from django.urls import path
from .views import details, random_article

urlpatterns = [
    path('<int:id>/', details, name='details'),
    path('', random_article, name='random_article')
]