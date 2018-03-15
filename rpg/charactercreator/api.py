from rest_framework import serializers, viewsets
from .models import Character, Fighter, Mage, Cleric, Thief, Necromancer, Zombie, Beast

# Serializers define the API representation.


class CharacterSerializer(serializers.ModelSerializer):
    inventory = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
 
    class Meta:
        model = Character
        fields = ('name', 'level', 'hp', 'character_id', 'exp', 'strength', 'intelligence', 'dexterity', 'wisdom', 'inventory')
# ViewSets define the view behavior.


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

print('GOT THIS FAR! In character api.py')