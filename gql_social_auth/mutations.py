
from gqlauth.core.mixins import ArgMixin
from mixins import SocialAuthMixin


class SocialAuth(ArgMixin):
    __doc__ = SocialAuthMixin.__doc__


# class SocialAuthJWT(ArgMixin):
#     __doc__ = JSONWebTokenMixin.__doc__
