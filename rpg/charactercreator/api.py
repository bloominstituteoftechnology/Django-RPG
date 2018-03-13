from rest_framework import serializers, viewsets
from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
# Serializers define the API representation.


class CharacterSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Character
        fields = ('name', 'level', 'hp', 'exp', 'strength',
                  'intelligence', 'dexterity', 'wisdom', 'inventory')


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
