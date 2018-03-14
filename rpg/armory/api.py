from rest_framework import viewsets, serializers
from .models import Items, Weapon

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Items
        fields = ('name', 'value', 'weight')
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer

class WeaponSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weapon
        fields = ('name', 'value', 'weight', 'power')
class WeaponViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer;