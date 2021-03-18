from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.News),
    path('Mems', views.Mems),
    path('HistoryCharacter', views.HistoryCharacter),
]