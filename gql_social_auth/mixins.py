from strawberry.types import Info
from gqlauth.user.resolvers import BaseMixin
from .types import SocialAuthInput
from social_django.utils import load_backend, load_strategy
from social_core.exceptions import MissingBackend
from django.utils.translation import gettext_lazy as _
from social_django.views import _do_login
from .types import SocialType

class SocialAuthMixin(BaseMixin):
    """
    aaa
    """
    @classmethod
    def resolve_mutation(cls, info: Info, input_: SocialAuthInput) -> SocialType:
        strategy = load_strategy(info.context)
        try:
            backend = load_backend(strategy, input_.provider, redirect_uri=None)

            authenticated_user = info.context.user if info.context.user.is_authenticated else None

            user = backend.do_auth(input_.access_token, user=authenticated_user)

            if user is None:
                return SocialType(success=False, errors=(_('Invalid token')))

            user_model = strategy.storage.user.user_model()

            if not isinstance(user, user_model):
                return SocialType(success=False, errors= _('`{}` is not a user instance').format(type(user).__name__))

            _do_login(backend, user, user.social_user)
            return SocialType.from_social_user(user)

        except MissingBackend:
            return SocialType(success=False, errors=_('Provider not found'))
        except Exception as e:
            return SocialType(success=False, errors=(_('{}'.format(e))))