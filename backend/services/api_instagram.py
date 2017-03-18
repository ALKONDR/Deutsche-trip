import urllib
import requests
import json
#import pandas as pd

client_id = 'c6605622c4714d6f802a6f3857fd8afb'
redirect_uri = 'http://127.0.0.1:5000/api/instagram/callback'
client_secret = json.load(open('secret.json'))['instagram']
base_url = 'https://api.instagram.com/oauth/authorize/'


def make_authorization_url():
    params = {"client_id": client_id,
              "response_type": "code",
              "redirect_uri": redirect_uri}
    url = base_url + "?" + urllib.parse.urlencode(params)
    return url


def get_token(code):
    print('Code: '+code)
    #client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    post_data = {"grant_type": "authorization_code",
                 "code": code,
                 "redirect_uri": redirect_uri,
                 'client_id': client_id,
                 'client_secret': client_secret}
    response = requests.post("https://api.instagram.com/oauth/access_token",
                            # auth=client_auth,
                             data=post_data)
    token_json = response.json()
    return token_json["access_token"], token_json['user']['id'], token_json['user']['username']


def get_photos(access_token, fr, to):

    return 0