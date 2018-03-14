from rest_framework import serializers, viewsets
from .models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item

# Serializers define the API representation.


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'value', 'weight')


class CharacterSerializer(serializers.HyperlinkedModelSerializer):

    inventory = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = ('name', 'level', 'exp', 'hp', 'strength',
                  'intelligence', 'dexterity', 'wisdom', 'inventory')

# ViewSets define the view behavior.


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
