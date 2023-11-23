from functools import wraps
from promise import Promise, is_thenable

from strawberry.types import Info
from social_django.utils import load_backend, load_strategy
from social_core.exceptions import MissingBackend
from gqlauth.core.constants import Messages as GQLMessages

from .types import SocialAuthInput
from .constants import Messages


def psa(f):
    @wraps(f)
    def wrapper(cls, info: Info, input_: SocialAuthInput, **kwargs):
        strategy = load_strategy()
        try:
            backend = load_backend(strategy, input_.provider, redirect_uri=None)

            user = backend.do_auth(input_.access_token)

            if user is None:
                return f(cls, info, input_, None, GQLMessages.INVALID_TOKEN, **kwargs)

            user_model = strategy.storage.user.user_model()

            if not isinstance(user, user_model):
                raise f(cls, info, input_, None, Messages.user_instance_error(user), **kwargs)

            return f(cls, info, input_, user, None, **kwargs)
        except MissingBackend:
            return f(cls, info, input_, None, Messages.NO_PROVIDER, **kwargs)
        except Exception as e:
            return f(cls, info, input_, None, Messages.exception(e), **kwargs)
    return wrapper


def social_auth(f):
    """
    Decorator for Getting social User. Use this decorator if you want to customize the SocialAuthMixin.
    :param f: Input: SocialAuthInput(provider, accessToken)
    :return: function with two additional arguments
        user: Entire User Object (Get your social data using user.social_user)
        errors: Any error occurred in the process of getting the Social User
    """
    @psa
    @wraps(f)
    def wrapper(cls, info, _input, user, errors, **kwargs):
        def on_resolve(payload):
            payload.user = user
            payload.errors = errors
            return payload

        result = f(cls, info, _input, user, errors, **kwargs)

        if is_thenable(result):
            return Promise.resolve(result).then(on_resolve)
        return on_resolve(result)

    return wrapper
