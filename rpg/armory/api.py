from rest_framework import serializers, viewsets
from .models import Item

# Serializers define the API representation.


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'value', 'weight')
# ViewSets define the view behavior.


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer