from rest_framework import serializers, viewsets
from .models import Character, Fighter

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
  inventory = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
  class Meta:
    model = Character
    fields = ('name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom', 'inventory')

# ViewSets define the view behavior.
class CharacterViewSet(viewsets.ModelViewSet):
  queryset = Character.objects.all()
  serializer_class = CharacterSerializer

class FighterSerializer(serializers.HyperlinkedModelSerializer):
  inventory = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
  class Meta:
    model = Fighter
    fields = ('name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom', 'using_shield', 'rage', 'inventory')

class FighterViewSet(viewsets.ModelViewSet):
  queryset = Fighter.objects.all()
  serializer_class = FighterSerializer
  