import graphene
import charactercreator.schema
import armory.schema

# from graphene_django.debug import DjangoDebug

class Query(armory.schema.Query, charactercreator.schema.Query, graphene.ObjectType):
    # debug = graphene.Field(DjangoDebug, name='__debug')
    pass

schema = graphene.Schema(query=Query)
