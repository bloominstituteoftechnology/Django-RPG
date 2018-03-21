from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('characters/', views.view_all_characters, name='characters'),
    path('character/<int:character_id>/', views.view_character, name='character'),
    path('character/<int:character_id>/items', views.view_all_items, name='items'),
    path('character/item/<int:item_id>/', views.view_all_items, name='items'),
]
