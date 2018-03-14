from django.urls import path,include, re_path
from rest_framework import routers, serializers, viewsets
from . import api

router = routers.DefaultRouter()
router.register(r'characters', api.CharacterViewSet)


app_name = 'show_characters'
urlpatterns = [
    re_path(r'^api/', include(router.urls)),
]
