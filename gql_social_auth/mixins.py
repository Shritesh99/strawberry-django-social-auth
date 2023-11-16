from strawberry.types import Info
from gqlauth.user.resolvers import BaseMixin
from gqlauth.core.constants import Messages as GQLMessages
from .types import SocialAuthInput
from social_django.utils import load_backend, load_strategy
from social_core.exceptions import MissingBackend

from .types import SocialType
from .constants import Messages


class SocialAuthMixin(BaseMixin):
    """Social Auth takes OAuth Provider and OAuth Access Token

    Allow user to perform social auth for the given OAuth provider and OAuth Access token
    """
    @classmethod
    def resolve_mutation(cls, info: Info, input_: SocialAuthInput) -> SocialType:
        strategy = load_strategy()
        try:
            backend = load_backend(strategy, input_.provider, redirect_uri=None)

            user = backend.do_auth(input_.access_token)

            if user is None:
                return SocialType(success=False, errors=GQLMessages.INVALID_TOKEN)

            user_model = strategy.storage.user.user_model()

            if not isinstance(user, user_model):
                return SocialType(success=False, errors=Messages.user_instance_error(user))

            return SocialType.from_social_user(user)

        except MissingBackend:
            return SocialType(success=False, errors=Messages.NO_PROVIDER)
        except Exception as e:
            return SocialType(success=False, errors=Messages.exception(e))
