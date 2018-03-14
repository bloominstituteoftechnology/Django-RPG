from rest_framework import serializers, viewsets
from .models import Item, Weapon
from charactercreator.models import Character

class ItemSerializer(serializers.RelatedField):
    def queryset():
        return None

    # def display_value(self, instance):
    #     return  "x"  #Item.objects.get(pk=instance).name

    def to_representation(self, instance):
        w = Weapon.objects.filter(pk=instance.item_id).exists()
        if w:
            return 'id: {4} name: {0} Weapon Power {1} value {2} weight {3}'.format(instance.name, instance.weapon.power,
            instance.value, instance.weight, instance.item_id)
        else:
            return 'id: {3} name: {0} value {1} weight {2}'.format(instance.name, instance.value, instance.weight,instance.item_id)         
    
    weapon=Weapon
    class Meta:
        model = Item
        fields = ('item_id', 'name', 'value', 'weight', 'weapon')

class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('power')

