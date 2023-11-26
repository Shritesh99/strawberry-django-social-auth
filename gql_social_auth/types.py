import strawberry
from typing import TYPE_CHECKING, Optional, cast, NewType
from django.conf import settings

from gqlauth.user.types_ import UserType
from gqlauth.core.utils import app_settings
from gqlauth.jwt.types_ import ObtainJSONWebTokenType, RefreshTokenType, TokenType
from gqlauth.models import RefreshToken


from .utils import dashed_to_camel

if TYPE_CHECKING:
    from gqlauth.core.utils import UserProto


@strawberry.input
class SocialAuthInput:
    provider: str
    access_token: str


SocialJSON = strawberry.scalar(
    NewType("SocialJSON", object),
    serialize=lambda value: dashed_to_camel(value),
    parse_value=lambda value: value
)


def resolve_extra_data(self, info) -> SocialJSON:
    if self.errors is not None:
        return None
    self.user.social_user.extra_data.pop('access_token', None)
    return self.user.social_user.extra_data


@strawberry.type
class SocialType(ObtainJSONWebTokenType):
    uid: Optional[str] = strawberry.field(
        description="User's uid", default=None)
    avatar: Optional[str] = strawberry.field(
        description="User's Avarar's URL", default=None)
    provider: Optional[str] = strawberry.field(
        description="OAUTH provider", default=None)
    extra_data: Optional[SocialJSON] = strawberry.field(
        description="Extra data requested from user",
        resolver=resolve_extra_data)

    @classmethod
    def from_social_user(cls, user) -> "SocialType":
        """
        Creates a new token and possibly a new refresh token based on the user.
        """
        ret = SocialType(
            success=True,
            user=cast(UserType, user),
            token=TokenType.from_user(user),
            uid=user.social_user.uid,
            provider=user.social_user.provider,
        )
        if hasattr(settings, 'SOCIAL_AUTH_PIPELINE') and 'gql_social_auth.pipeline.get_avatar' in settings.SOCIAL_AUTH_PIPELINE:
            ret.avatar = user.avatar
        if app_settings.JWT_LONG_RUNNING_REFRESH_TOKEN:
            ret.refresh_token = cast(RefreshTokenType, RefreshToken.from_user(user))
        return ret
