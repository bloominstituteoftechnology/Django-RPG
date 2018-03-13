from django.urls import path

from . import views
app_name = 'show_characters'
urlpatterns = [
    path('', views.index, name='index'),
    path('characters/', views.view_all_characters, name='characters'),
    path('characters/<int:character_id>/', views.view_character,name='character' ),
]
