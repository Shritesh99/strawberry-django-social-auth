
from gqlauth.core.mixins import ArgMixin
from .mixins import SocialAuthMixin


class SocialAuth(SocialAuthMixin, ArgMixin):
    __doc__ = SocialAuthMixin.__doc__
