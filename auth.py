import os
from requests_oauthlib import OAuth1Session


def getRequestToken(oauth):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    fetch_response = oauth.fetch_request_token(request_token_url)
    resource_owner_key = fetch_response.get('oauth_token')
    resource_owner_secret = fetch_response.get('oauth_token_secret')
    return resource_owner_key, resource_owner_secret


def getAuth(oauth):
    base_authorization_url = 'https://api.twitter.com/oauth/authenticate'
    authorization_url = oauth.authorization_url(base_authorization_url)
    print('Authorise this app and copy the pin: %s' % authorization_url)
    verifier = input('Paste the PIN here: ')
    return verifier


def getAccessToken(consumer_key, consumer_secret, resource_owner_key,
                   resource_owner_secret, verifier):
    access_token_url = 'https://api.twitter.com/oauth/access_token'
    oauth = OAuth1Session(consumer_key,
                          client_secret=consumer_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret,
                          verifier=verifier)
    oauth_tokens = oauth.fetch_access_token(access_token_url)
    return oauth_tokens


def createOAuthSession(consumer_key, consumer_secret):
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
    return oauth


def authSetup():
    consumer_key = os.environ.get('PUBLIC_KEY')  # Add your API key here
    consumer_secret = os.environ.get('SECRET_KEY')  # Add your API secret key here
    oauth = createOAuthSession(consumer_key, consumer_secret)
    resource_owner_key, resource_owner_secret = getRequestToken(oauth)
    verifier = getAuth(oauth)
    oauth_tokens = getAccessToken(consumer_key, consumer_secret, resource_owner_key,
                                  resource_owner_secret, verifier)
    access_token = oauth_tokens['oauth_token']
    access_token_secret = oauth_tokens['oauth_token_secret']
    oauth = OAuth1Session(consumer_key,
                          client_secret=consumer_secret,
                          resource_owner_key=access_token,
                          resource_owner_secret=access_token_secret)
    return oauth
