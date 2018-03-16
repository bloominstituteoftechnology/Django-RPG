from rest_framework import serializers, viewsets
from .models import Item, Weapon

WEAPON_IDS = set(Weapon.objects.values_list('item_id', flat=True))


def is_weapon(item):
    print(item)
    return item.item_id in WEAPON_IDS

# Serializers define the API representation.


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    is_weapon = serializers.BooleanField(source='is_weapon')

    class Meta:
        model = Item
        fields = ('name', 'value', 'weight')

# ViewSets define the view behavior.


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
