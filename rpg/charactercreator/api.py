from rest_framework import serializers, viewsets
from .models import Character, Fighter, Mage, Cleric, Thief, Necromancer, Zombie, Beast

# Serializers define the API representation.


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ('name', 'level', 'hp', 'character_id', 'exp', 'strength', 'intelligence', 'dexterity', 'wisdom')
# ViewSets define the view behavior.


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    