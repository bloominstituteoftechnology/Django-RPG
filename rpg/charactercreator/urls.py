from django.urls import path,include, re_path
from rest_framework import routers, serializers, viewsets
from . import api

<<<<<<< HEAD
from . import views
app_name = 'show_characters'
urlpatterns = [
    path('', views.index, name='index'),
    path('characters/', views.view_all_characters, name='characters'),
    path('characters/<int:character_id>/', views.view_character,name='character' )
=======
router = routers.DefaultRouter()
router.register(r'characters', api.CharacterViewSet)


app_name = 'show_characters'
urlpatterns = [
    re_path(r'^api/', include(router.urls)),
>>>>>>> my_api
]
