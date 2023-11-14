import strawberry
from gql_social_auth import mutations
from gqlauth.core.middlewares import JwtSchema
from gqlauth.user.queries import UserQueries

@strawberry.type
class Mutation:
    social_auth = mutations.SocialAuth.field


@strawberry.type
class Query(UserQueries):
    pass


arg_schema = JwtSchema(query=Query, mutation=Mutation)

