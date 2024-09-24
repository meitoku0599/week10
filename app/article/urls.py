from django.urls import path
from . import views

app_name= 'article'
urlpatterns = [
    path('', views.index, name='index'),
    path('articles', views.article_list, name='article_list'),
    path('articles/<uuid:uuid>', views.article_detail, name='article_detail'),    
]