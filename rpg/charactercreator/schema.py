from graphene_django import DjangoObjectType
import graphene
from .models import Character as CharacterModel
from rpg.armory.models import  Item as ItemModel, Weapon as WeaponModel
from graphene_django.filter import DjangoFilterConnectionField


class Weapon(DjangoObjectType):
    class Meta:
        model = WeaponModel
        
class Item(DjangoObjectType):
    graphene.Field(Weapon)
    class Meta:
        model = ItemModel
        interfaces = (graphene.relay.Node, )        
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'value': ['exact', 'lt', 'gt'],
            'weight': ['exact', 'lt', 'gt'],
            'power': ['exact', 'lt', 'gt'],
        }        






class CharacterNode(DjangoObjectType):
    inventory = graphene.List(Item)

    def resolve_inventory(self, info):
        return self.inventory.all()
    
    class Meta:
        model = CharacterModel
        interfaces = (graphene.relay.Node, )
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'level': ['exact', 'lt', 'gt'],
        }

class Query(graphene.ObjectType):
    all_characters = DjangoFilterConnectionField(CharacterNode)   

schema = graphene.Schema(query=Query)


