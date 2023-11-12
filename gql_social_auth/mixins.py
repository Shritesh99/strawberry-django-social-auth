from strawberry.types import Info
from gqlauth.user.resolvers import BaseMixin
from .types import SocialAuthInput
from social_django.utils import load_backend, load_strategy
from social_core.exceptions import MissingBackend
from gqlauth.core.exceptions import GraphQLAuthError
from django.utils.translation import gettext_lazy as _
from social_django.views import _do_login
from .types import SocialType

from django.contrib.auth.models import AbstractUser
class SocialAuthMixin(BaseMixin):
    """
    aaa
    """
    @classmethod
    def resolve_mutation(cls, info: Info, input_: SocialAuthInput):
        strategy = load_strategy(info.context)

        try:
            backend = load_backend(strategy, input_.provider, redirect_uri=None)
        except MissingBackend:
            raise GraphQLAuthError(_('Provider not found'))
        if info.context.user.is_authenticated:
            authenticated_user = info.context.user
        else:
            authenticated_user = None
        try:
            user = backend.do_auth(input_.access_token, user=authenticated_user)

            if user is None:
                raise GraphQLAuthError(_('Invalid token'))

            user_model = strategy.storage.user.user_model()

            if not isinstance(user, user_model):
                msg = _('`{}` is not a user instance').format(type(user).__name__)
                raise GraphQLAuthError(msg)

            _do_login(backend, user, user.social_user)
            return SocialType.from_social_user(user)

        except Exception as e:
            raise GraphQLAuthError(_('{}'.format(e)))


# class JSONWebTokenMixin:
#     """
#     aaa
#     """
#     token: str
#
#     @classmethod
#     def resolve(cls, root, info, social, **kwargs):
#         return cls(token=get_token(social.user))
