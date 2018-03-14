from rest_framework import serializers, viewsets
from .models import Weapon, Item

class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ('name', 'value', 'weight', 'power')

class WeaponViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer