[![Tests](https://img.shields.io/github/actions/workflow/status/shritesh99/strawberry-django-social-auth/tests.yml?label=Tests&style=for-the-badge)](https://github.com/shritesh99/strawberry-django-social-auth/actions/workflows/tests.yml)

[![Codecov](https://img.shields.io/codecov/c/github/shritesh99/strawberry-django-social-auth?style=for-the-badge)](https://app.codecov.io/gh/shritesh99/strawberry-django-social-auth)

[![Pypi](https://img.shields.io/pypi/v/strawberry-django-social-auth.svg?style=for-the-badge&logo=appveyor)](https://pypi.org/project/strawberry-django-social-auth/)

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=for-the-badge&logo=appveyor)](https://github.com/shritesh99/strawberry-django-social-auth/blob/main/CONTRIBUTING.md)

[![Pypi downloads](https://img.shields.io/pypi/dm/strawberry-django-social-auth?style=for-the-badge)](https://pypistats.org/packages/strawberry-django-social-auth)

[![Python versions](https://img.shields.io/pypi/pyversions/strawberry-django-social-auth?style=social)](https://pypi.org/project/strawberry-django-social-auth/)

# Strawberry-django Social Auth
[Django](https://github.com/django/django)  social authentication with [Strawberry](https://strawberry.rocks/) using [Social Django](https://github.com/Shritesh99/strawberry-django-social-auth/).

## About
#### This Library was inspired by [Django-graphql-social-auth](https://github.com/flavors/django-graphql-social-auth).

Django Social Auth for Strawberry Graphql engine.  

### Docs can be found [here](https://shritesh99.github.io/strawberry-django-social-auth/)

## Features

* [x] Awesome docs!
* [X] Social Auth
* [x] Profile pic's URL storage in User's model  
* [ ] Relay Support (Coming Soon...)

### Installation:
```python
pip install strawberry-django-social-auth
```
- Add this for Avatar support in `settings.py`
```python

SOCIAL_AUTH_PIPELINE = [
    ...
    'gql_social_auth.pipeline.get_avatar',  # Get Avatar Pipeline
]
```

### Usage:
1. Use built-In Mutation
```python
@strawberry.type
class Mutation:
    social_auth = mutations.SocialAuth.field

schema = strawberry.Schema(query=Query, mutation=Mutation)
```
2. Customize the Usage of Mutation using the decorator
```python
from gql_social_auth.decorators import social_auth
from gql_social_auth.types import SocialAuthInput

@strawberry.type
class CustomMutation:
    @strawberry.mutation
    @social_auth
    def social_auth(self, info: Info, _input: SocialAuthInput, user, errors) -> CustomReturnType:
        # user: User object from model
        # errors: If any errors occurred during the process of getting the social auth
        # Note: Any of the user or errors is None at a time, both can't be None at the same time...
        if errors is not None:
            # Handle Error here
        # Use user Object here... 
        
```

#### Calling:
```
mutation SocialAuth($provider: String!, $accessToken: String!){
    socialAuth(provider: $provider, accessToken: $accessToken){
        uid
        avatar
        extraData
        errors
        success
        refreshToken {
            created
            isExpired
            expiresAt
            token
            revoked
        }
        token {
            token
            payload {
                exp
                origIat
            }
        }
        user {
            email
            archived
            dateJoined
            firstName
            isActive
            id
            isStaff
            isSuperuser
            lastLogin
            lastName
            logentrySet {
                pk
            }
            status {
                archived
                verified
            }
            verified
        }
      }
    }
```


## Contributing

See [CONTRIBUTING.md](https://github.com/Shritesh99/strawberry-django-social-auth/blob/main/CONTRIBUTING.md)