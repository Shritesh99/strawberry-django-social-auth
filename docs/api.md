
> auto generated using `pydoc_markdown`
___
## SocialAuthMixin

```python
class SocialAuthMixin(BaseMixin)
```

> Social Auth takes OAuth Provider and OAuth Access Token
> 
> Allow user to perform social auth for the given OAuth provider and OAuth Access token
> :returns
>     user: Entire User Object (Get your social data using user.social_user)
>     errors: Any error occurred in the process of getting the Social User

## social\_auth

```python
def social_auth(f)
```

> Decorator for Getting social User. Use this decorator if you want to customize the SocialAuthMixin.
> :param f: Input: SocialAuthInput(provider, accessToken)
> :return: function with two additional arguments
>     user: Entire User Object (Get your social data using user.social_user)
>     errors: Any error occurred in the process of getting the Social User


