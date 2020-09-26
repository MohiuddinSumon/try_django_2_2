import graphene
import platforms.schema


class Query(platforms.schema.Query, graphene.ObjectType):
    pass


# Mutation
class Mutation(platforms.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
