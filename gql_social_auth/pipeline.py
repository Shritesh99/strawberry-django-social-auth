def get_avatar(backend, strategy, details, response, user=None, is_new=False, *args, **kwargs):
    if not is_new:
        return
    url = None
    if backend.name == "facebook":
        # The main part is how to get the profile picture URL and then do what you need to do
        url = 'https://graph.facebook.com/{0}/picture/?type=large&access_token={1}'.format(response['id'],
                                                                                           response['access_token'])
    elif backend.name == 'google-oauth2':
        url = response['picture']
    if backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal', '')
    if url:
        user.avatar = url
        user.save()
