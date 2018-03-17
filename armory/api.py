from rest_framework import serializers, viewsets
from .models import Item, Weapon
# from charactercreator.models import Character

class ItemSerializer(serializers.RelatedField):
    # def queryset():
    #     return None

    # def display_value(self, item):
    #     return  "x"  #Item.objects.get(pk=item).name

    def to_representation(self, item):
        w =  hasattr(item,"weapon") #Weapon.objects.filter(pk=item.item_id).exists()
        if w:
            return 'id: {4} name: {0} Weapon Power {1} value {2} weight {3}'.format(item.name, item.weapon.power,
            item.value, item.weight, item.item_id)
        else:
            return 'id: {3} name: {0} value {1} weight {2}'.format(item.name, item.value, item.weight,item.item_id)         
    
    weapon=Weapon
    class Meta:
        model = Item
        fields = ('item_id', 'name', 'value', 'weight', 'weapon')

class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('power')

