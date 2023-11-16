[//]: # ([![Tests]&#40;https://img.shields.io/github/actions/workflow/status/nrbnlulu/strawberry-django-auth/tests.yml?label=Tests&style=for-the-badge&#41;]&#40;https://github.com/nrbnlulu/strawberry-django-auth/actions/workflows/tests.yml&#41;)

[//]: # ([![Codecov]&#40;https://img.shields.io/codecov/c/github/nrbnlulu/strawberry-django-auth?style=for-the-badge&#41;]&#40;https://app.codecov.io/gh/nrbnlulu/strawberry-django-auth&#41;)

[//]: # ([![Pypi]&#40;https://img.shields.io/pypi/v/strawberry-django-auth.svg?style=for-the-badge&logo=appveyor&#41;]&#40;https://pypi.org/project/strawberry-django-auth/&#41;)

[//]: # ([![contributions welcome]&#40;https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=for-the-badge&logo=appveyor&#41;]&#40;https://github.com/nrbnlulu/strawberry-django-auth/blob/main/CONTRIBUTING.md&#41;)

[//]: # ([![Pypi downloads]&#40;https://img.shields.io/pypi/dm/strawberry-django-auth?style=for-the-badge&#41;]&#40;https://pypistats.org/packages/strawberry-django-auth&#41;)

[//]: # ([![Python versions]&#40;https://img.shields.io/pypi/pyversions/strawberry-django-auth?style=social&#41;]&#40;https://pypi.org/project/strawberry-django-auth/&#41;)

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