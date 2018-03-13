from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path, re_path
from rest_framework import routers, serializers, viewsets
from charactercreator.api import CharacterViewSet

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

urlpatterns = [
    path('charactercreator/', include('charactercreator.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^api/', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls')),
]