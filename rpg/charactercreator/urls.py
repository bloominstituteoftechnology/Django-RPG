from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('characters/', views.view_all_characters, name='characters'),
    path('characters/{0}', views.view_character, name='character'),
]
