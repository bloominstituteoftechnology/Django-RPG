from graphene_django import DjangoObjectType
from graphene import ObjectType, List, Schema, relay
from .models import Character as CharacterModel, Item as ItemModel
from graphene_django.filter import DjangoFilterConnectionField

class CharacterNode(DjangoObjectType):
  class Meta:
    model = CharacterModel
    interfaces = (relay.Node, )
    filter_fields = {
      'name': ['exact', 'icontains', 'istartswith'],
      'level': ['exact', 'lt', 'gt'],
    }


class Item(DjangoObjectType):
  class Meta:
    model = ItemModel

class Query(ObjectType):
  characters = List(CharacterNode)
  def resolve_characters(self, info):
    return CharacterModel.objects.all()

  # all_characters = DjangoFilterConnectionField(CharacterNode)

  def resolve_items(self, info):
    return ItemModel.objects.all()

schema = Schema(query=Query)