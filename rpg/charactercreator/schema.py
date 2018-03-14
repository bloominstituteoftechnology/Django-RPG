from graphene_django import DjangoObjectType
import graphene
from .models import Character as CharacterModel

class Character(DjangoObjectType):
    class Meta:
        model = CharacterModel

class Query(graphene.ObjectType):
    characters = graphene.List(Character)

    def resolve_characters(self, info):
        return CharacterModel.objects.all()

schema = graphene.Schema(query=Query)
