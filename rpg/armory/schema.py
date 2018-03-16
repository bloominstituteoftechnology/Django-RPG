from graphene_django import DjangoObjectType
import graphene
from .models import Item as ItemModel

class Item(DjangoObjectType):
    class Meta:
        model = ItemModel

class Query(graphene.ObjectType):
    items = graphene.List(Item)

    def resolve_items(self, info):
        return ItemModel.objects.all()

schema = graphene.Schema(query=Query)