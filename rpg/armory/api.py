from rest_framework import serializers, viewsets
from rpg.armory.models import Item

# Serializers define the API representation.


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'weight', 'value')
# ViewSets define the view behavior.



class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
