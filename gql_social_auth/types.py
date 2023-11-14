import strawberry
from typing import TYPE_CHECKING, Optional, cast, NewType

from gqlauth.user.types_ import UserType
from gqlauth.core.utils import app_settings, inject_fields
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
    self.extra_data.pop('access_token', None)
    return self.extra_data


@strawberry.type
class SocialType(ObtainJSONWebTokenType):
    uid: Optional[str] = strawberry.field(
        description="User's uid", default=None)
    provider: Optional[str] = strawberry.field(
        description="OAUTH provider", default=None)
    extra_data: Optional[SocialJSON] = strawberry.field(
        description="Extra data requested from user",
        resolver=resolve_extra_data)

    @classmethod
    def from_social_user(cls, user) -> "SocialType":
        """Creates a new token and possibly a new refresh token based on the
        user.

        *call this method only for trusted users.*
        """
        ret = SocialType(
            success=True,
            user=cast(UserType, user),
            token=TokenType.from_user(user),
            uid=user.uid,
            provider=user.provider,
            extra_data=user.extra_data
        )
        if app_settings.JWT_LONG_RUNNING_REFRESH_TOKEN:
            ret.refresh_token = cast(RefreshTokenType, RefreshToken.from_user(user))
        return ret

    # @classmethod
    # def authenticate(cls, info: Info, input_: SocialAuthInput) -> "ObtainJSONWebTokenType":
    #     """Return `ObtainJSONWebTokenType`. authenticates against django
    #     authentication backends.
    #
    #     *creates a new token and possibly a refresh token.*
    #     """
    #     args = {
    #         "provider": input_.provider,
    #         "auth_token": input_.access_tokeen,
    #     }
    #     try:
    #         strategy = load_strategy(info.context)
    #
    #         user: Optional["UserProto"]
    #
    #         backend = load_backend(
    #             strategy, args["provider"], redirect_uri=None)
    #
    #         if info.context.user.is_authenticated:
    #             authenticated_user = info.context.user
    #         else:
    #             authenticated_user = None
    #
    #         user = backend.do_auth(
    #             args["access_token"], user=authenticated_user)
    #
    #         if user is None:
    #             raise exceptions.InvalidTokenError(_('Invalid token'))
    #
    #         from gqlauth.models import UserStatus, RefreshToken
    #
    #         status: UserStatus = getattr(user, "status")  # noqa: B009
    #         # gqlauth logic
    #         if status.archived is True:  # un-archive on login
    #             UserStatus.unarchive(user)
    #         if status.verified or app_settings.ALLOW_LOGIN_NOT_VERIFIED:
    #             # successful login.
    #             user.last_login = localtime()
    #             user.save(update_fields=("last_login",))
    #             ret = ObtainJSONWebTokenType(
    #                 success=True, user=cast(UserType, user), token=TokenType.from_user(user)
    #             )
    #             if app_settings.JWT_LONG_RUNNING_REFRESH_TOKEN:
    #                 ret.refresh_token = cast(
    #                     RefreshTokenType, RefreshToken.from_user(user))
    #         else:
    #             return ObtainJSONWebTokenType(success=False, errors=Messages.NOT_VERIFIED)
    #
    #     except MissingBackend:
    #         raise exceptions.GraphQLSocialAuthError(
    #             _('Provider not found'))
    #
    #     except PermissionDenied:
    #         # one of the authentication backends rejected the user.
    #         return ObtainJSONWebTokenType(success=False, errors=Messages.UNAUTHENTICATED)
    #
    #     except TokenExpired:
    #         return ObtainJSONWebTokenType(success=False, errors=Messages.EXPIRED_TOKEN)
