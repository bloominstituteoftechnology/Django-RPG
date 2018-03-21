from rest_framework import serializers, viewsets
from .models import Item

class ItemSerializer(serializers.HyperlinkedModelSerializer):
  is_weapon = serializers.BooleanField(source='weapon.is_weapon')
  
  class Meta:
    model = Item
    fields = ('name', 'value', 'weight', 'is_weapon')

class ItemViewSet(viewsets.ModelViewSet):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
