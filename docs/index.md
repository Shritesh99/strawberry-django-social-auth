[![Tests](https://img.shields.io/github/actions/workflow/status/shritesh99/strawberry-django-social-auth/tests.yml?label=Tests&style=for-the-badge)](https://github.com/shritesh99/strawberry-django-social-auth/actions/workflows/tests.yml)

[![Codecov](https://img.shields.io/codecov/c/github/shritesh99/strawberry-django-social-auth?style=for-the-badge)](https://app.codecov.io/gh/shritesh99/strawberry-django-social-auth)

[![Pypi](https://img.shields.io/pypi/v/strawberry-django-social-auth.svg?style=for-the-badge&logo=appveyor)](https://pypi.org/project/strawberry-django-social-auth/)

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=for-the-badge&logo=appveyor)](https://github.com/shritesh99/strawberry-django-social-auth/blob/main/CONTRIBUTING.md)

[![Pypi downloads](https://img.shields.io/pypi/dm/strawberry-django-social-auth?style=for-the-badge)](https://pypistats.org/packages/strawberry-django-social-auth)

[![Python versions](https://img.shields.io/pypi/pyversions/strawberry-django-django-auth?style=social)](https://pypi.org/project/strawberry-django-social-auth/)

# Strawberry-django Social Auth
[Django](https://github.com/django/django)  social authentication with [Strawberry](https://strawberry.rocks/) using [Social Django](https://github.com/Shritesh99/strawberry-django-social-auth/).

## About
#### This Library was inspired by [Django-graphql-social-auth](https://github.com/flavors/django-graphql-social-auth).

Django Social Auth for Strawberry Graphql engine.  

### Docs can be found [here](https://shritesh99.github.io/strawberry-django-social-auth/)

## Features

* [x] Awesome docs!
* [X] Social Auth

### Full schema features

```python
@strawberry.type
class Mutation:
    social_auth = mutations.SocialAuth.field

schema = strawberry.Schema(query=Query, mutation=Mutation)
```

## Contributing

See [CONTRIBUTING.md](https://github.com/Shritesh99/strawberry-django-social-auth/blob/main/CONTRIBUTING.md)