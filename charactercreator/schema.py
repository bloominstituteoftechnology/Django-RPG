from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene
from .models import Character as CharacterModel

class CharacterNode(DjangoObjectType):
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
