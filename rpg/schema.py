import graphene
import rpg.charactercreator.schema

class Query(charactercreator.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)