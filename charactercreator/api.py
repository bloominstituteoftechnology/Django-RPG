from rest_framework import serializers, viewsets
from .models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon
from armory.api import ItemSerializer
# Serializers define the API representation.
class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    inventory = ItemSerializer(many=True, read_only=False )
    class Meta:
        model = Character
        fields = ('character_id','name', 'level', 'exp', 'hp', 'strength', 'intelligence',
        'dexterity', 'wisdom', 'inventory'
        )

# ViewSets define the view behavior.
class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer