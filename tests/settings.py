from gqlauth.settings_type import GqlAuthSettings

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'social_django',
    "strawberry_django",
    "gqlauth",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

SECRET_KEY = 'test'

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
]

GQL_AUTH = GqlAuthSettings(
    LOGIN_REQUIRE_CAPTCHA=True,
    REGISTER_REQUIRE_CAPTCHA=True,
    CAPTCHA_SAVE_IMAGE=True,
    SEND_ACTIVATION_EMAIL=False,
)
