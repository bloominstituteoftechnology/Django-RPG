from rest_framework import serializers, viewsets
from .models import Character, Fighter, Mage, Cleric, Thief, Necromancer, Assassin, GrandWizard

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ('name', 'level')
class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer