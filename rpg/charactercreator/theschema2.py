# we need to import the object types
# the graphene package to access graphql
# create me a CharacterModel
# create me an ItemModel

from graphene_django import DjangoObjectType
import graphene
from .models import Character as CharacterModel
from .models import Item as ItemModel 

# Item is a django object, create a class for it, and call it ItemModel
class Item(DjangoObjectType):
    class Meta:
        model = ItemModel

# Character is also a django object, create a class for it, and call it CharacterModel
class Character(DjangoObjectType):
    class Meta:
        model = CharacterModel

# create a query that looks to inventory and characters
class Query(graphene.ObjectType):
    inventory = graphene.List(Item)
    characters = graphene.List(Character)

# resolve the character model
    def resolve_characters(self, info):
        return CharacterModel.objects.all()

# resolve the item model
    def resolve_items(self, info):
        return ItemModel.objects.all()

# set the schema to the above
schema = graphene.Schema(query=Query)