from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [

    path('', views.startpage, name='startpage'),
    path('<slug>/', views.article_detail, name='article_detail'),




]
