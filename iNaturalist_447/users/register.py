from authlib.integrations.django_client import OAuth
from datetime import timedelta
oauth = OAuth()

# decorator for routes that should be accessible only by logged in users
from auth_decorator import login_required

AUTHLIB_OAUTH_CLIENTS = {
    'twitter': {
        'client_id': 'Twitter Consumer Key',
        'client_secret': 'Twitter Consumer Secret',
        'request_token_url': 'https://api.twitter.com/oauth/request_token',
        'request_token_params': None,
        'access_token_url': 'https://api.twitter.com/oauth/access_token',
        'access_token_params': None,
        'refresh_token_url': None,
        'authorize_url': 'https://api.twitter.com/oauth/authenticate',
        'api_base_url': 'https://api.twitter.com/1.1/',
        'client_kwargs': None
    }
}

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware'
]
def login(request):
    # build a full authorize callback uri
    redirect_uri = request.build_absolute_uri('/authorize')
    return oauth.twitter.authorize_redirect(request, redirect_uri)
from django.dispatch import receiver
from authlib.integrations.django_client import token_update

@receiver(token_update)
def on_token_update(sender, token, refresh_token=None, access_token=None):
    if refresh_token:
        item = OAuth2Token.find(name=name, refresh_token=refresh_token)
    elif access_token:
        item = OAuth2Token.find(name=name, access_token=access_token)
    else:
        return

    # update old token
    item.access_token = token['access_token']
    item.refresh_token = token.get('refresh_token')
    item.expires_at = token['expires_at']
    item.save()
