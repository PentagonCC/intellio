from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('load_news/', views.load_news, name='load_news'),
]
