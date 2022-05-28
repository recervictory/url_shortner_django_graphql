import graphene
# Todo: Import App schema to main project schema
import shortener.schema

# Todo: Create all main Query
class Query(shortener.schema.Query, graphene.ObjectType):
    pass

# Todo: create all Mutation 
class Mutation(shortener.schema.Mutation, graphene.ObjectType):
    pass

# Todo: Export Schema Variable
schema = graphene.Schema(query=Query, mutation=Mutation)


