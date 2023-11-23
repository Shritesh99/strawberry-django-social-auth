from strawberry.types import Info
from gqlauth.user.resolvers import BaseMixin
from .decorators import social_auth
from .types import SocialAuthInput
from .types import SocialType


class SocialAuthMixin(BaseMixin):
    """Social Auth takes OAuth Provider and OAuth Access Token

    Allow user to perform social auth for the given OAuth provider and OAuth Access token
    :returns
        user: Entire User Object (Get your social data using user.social_user)
        errors: Any error occurred in the process of getting the Social User
    """

    @classmethod
    @social_auth
    def resolve_mutation(cls, info: Info, input_: SocialAuthInput, user, errors) -> SocialType:
        if errors is not None:
            return SocialType(success=False, errors=errors)
        return SocialType.from_social_user(user)
