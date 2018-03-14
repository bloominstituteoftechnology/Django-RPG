from rest_framework import serializers, viewsets
from .models import Item, Weapon

class ItemSerializer(serializers.ModelSerializer):
    is_weapon = serializers.BooleanField(source='weapon.is_weapon')

    class Meta:
        model = Item
        fields = ('name', 'value', 'weight', 'is_weapon')

# ViewSets define the view behavior.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
