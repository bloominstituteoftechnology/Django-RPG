from django.urls import path, include

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('characters/', views.view_all_characters, name='characters'),
    path('character/<int:character_id>/', views.view_character, name='character'),
]
