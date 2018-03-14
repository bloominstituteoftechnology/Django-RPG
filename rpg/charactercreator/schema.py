from graphene_django import DjangoObjectType
from graphene import relay
import graphene
from .models import Character as CharacterModel
from .models import Item as ItemModel


class Item(DjangoObjectType):
    class Meta:
        model = ItemModel


class Character(DjangoObjectType):

    class Meta:
        model = CharacterModel


class Query(graphene.ObjectType):
    inventory = graphene.List(Item)
    characters = graphene.List(Character)

    def resolve_characters(self, info):
        return CharacterModel.objects.all()

    def resolve_items(self, info):
        return ItemModel.objects.all()


schema = graphene.Schema(query=Query)
