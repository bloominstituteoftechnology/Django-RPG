from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path, re_path
from rest_framework import routers, serializers, viewsets
from graphene_django.views import GraphQLView
from django.shortcuts import render


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # def to_representation(self, user):
    #     return 'username {0} email {1} is_staff {2}'.format(user.username, user.email, user.is_staff)

    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def view_user(request):
     return render(request, 'user.html', None)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('charactercreator/', include('charactercreator.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^accounts/profile/',view_user),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^api/', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r'^$', GraphQLView.as_view(graphiql=True), None, 'GraphIQL'),    
]