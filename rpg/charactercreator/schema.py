from graphene_django import DjangoObjectType
import graphene
from .models import Character as CharacterModel
from .models import Item as ItemModel

class Character(DjangoObjectType):
    class Meta:
        model = CharacterModel

class Item(DjangoObjectType):
    class Meta:
        model = ItemModel

class Query(graphene.ObjectType):
    characters = graphene.List(Character)
    inventory = graphene.List(Item)

    def resolve_items(self, info):
        return ItemModel.objects.all()

    def resolve_characters(self, info):
        return CharacterModel.objects.all()

schema = graphene.Schema(query=Query)