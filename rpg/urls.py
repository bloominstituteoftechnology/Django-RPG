from django.conf.urls import include, url
# from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views


# from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path, re_path
from rest_framework import routers, serializers, viewsets
from charactercreator.api import CharacterViewSet
from graphene_django.views import GraphQLView

# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'characters', CharacterViewSet)
# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    # url(r'^$', hello.views.index, name='index'),
    # url(r'^db', hello.views.db, name='db'),
    path('admin/', admin.site.urls),
    path('charactercreator/', include('charactercreator.urls')),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^api/', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r'^graphql/', GraphQLView.as_view(graphiql=True)),
]
