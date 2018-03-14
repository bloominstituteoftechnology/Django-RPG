"""rpg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from charactercreator.api import CharacterViewSet
from armory.api import ItemViewSet
from graphene_django.views import GraphQLView


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'characters', CharacterViewSet)
router.register(r'items', ItemViewSet)


urlpatterns = [
    path('charactercreator/', include('charactercreator.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^api/', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r'^graphql/', GraphQLView.as_view(graphiql=True)),
]
