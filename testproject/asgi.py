"""
ASGI config for testproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testproject.settings")

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from gqlauth.core.middlewares import channels_jwt_middleware
from strawberry.channels import GraphQLHTTPConsumer

from testproject.schema import arg_schema


gql_http_consumer = AuthMiddlewareStack(
    channels_jwt_middleware(GraphQLHTTPConsumer.as_asgi(schema=arg_schema))
)
application = ProtocolTypeRouter(
    {
        "http": URLRouter(
            [
                re_path("^graphql", gql_http_consumer),
            ]
        ),
    }
)
