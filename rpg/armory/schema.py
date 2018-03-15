from graphene_django import DjangoObjectType
import graphene
from .models import Item as ItemModel
from .models import Weapon as WeaponModel

class Item(DjangoObjectType):
    class Meta:
        model = ItemModel

class Weapon(DjangoObjectType):
    class Meta:
        model = WeaponModel

class Query(graphene.ObjectType):
    items = graphene.List(Item)
    weapons = graphene.List(Weapon)

    def resolve_items(self, info):
        return ItemModel.objects.all()

    def resolve_weapons(self, info):
        return WeaponModel.objects.all()


schema = graphene.Schema(query=Query)