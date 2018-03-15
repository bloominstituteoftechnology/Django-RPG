import graphene
import rpg.charactercreator.schema
import rpg.armory.schema

# from graphene_django.debug import DjangoDebug

class Query(rpg.armory.schema.Query, rpg.charactercreator.schema.Query, graphene.ObjectType):
    # debug = graphene.Field(DjangoDebug, name='__debug')
    pass

schema = graphene.Schema(query=Query)
