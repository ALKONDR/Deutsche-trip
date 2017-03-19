import urllib
import requests
import json
import pandas as pd

client_id = 'aff8e8e9-0f5d-4fb7-8f9f-ce19fbef6b5c'
client_secret = json.load(open('secret.json'))['client_secret']
redirect_uri = "http://127.0.0.1:5000/api/deutsche/callback"
base_url = "https://simulator-api.db.com/gw/oidc/authorize"


def make_authorization_url():
    params = {"client_id": client_id,
              "response_type": "code",
              "state": redirect_uri,
              "redirect_uri": redirect_uri}
    url = base_url + "?" + urllib.parse.urlencode(params)
    return url


def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    post_data = {"grant_type": "authorization_code",
                 "code": code,
                 "redirect_uri": redirect_uri}
    response = requests.post("https://simulator-api.db.com/gw/oidc/token",
                             auth=client_auth,
                             data=post_data)
    token_json = response.json()
    return token_json["access_token"]


def get_cashAccounts(access_token):
    trans_url = 'https://simulator-api.db.com/gw/dbapi/v1/cashAccounts'
    headers = {"Authorization": "bearer " + access_token}
    response = requests.get(trans_url, headers=headers)
    response = response.json()
#     s = ''
#     for i in range(len(response)):
#         s += "iban: "+response[i]['iban'] + "<br/> balance: " + str(response[i]['balance']) +\
#             '<br/> productDescription: ' + response[i]['productDescription'] + '<br/><br/>' 
    return response


# get all of user transactions 
def get_transactions(access_token):
    trans_url = 'https://simulator-api.db.com/gw/dbapi/v1/transactions'
    headers = {"Authorization": "bearer " + access_token}
    response = requests.get(trans_url, headers=headers)
    response = response.json()
#     s = ''
#     for i in range(len(response)):
#         s += "iban: "+response[i]['originIban'] + "<br/> amount: " + str(response[i]['amount']) +\
#             '<br/> bookingDate: ' + response[i]['bookingDate'] 
#         if 'counterPartyName' in response[i]:
#             s += '<br/> counterPartyName: ' + response[i]['counterPartyName']
#         if 'counterPartyIban' in response[i]:
#             s += '<br/> counterPartyIban: ' + response[i]['counterPartyIban']
#         if 'usage' in response[i]:
#             s += '<br/> usage: ' + response[i]['usage']            
#         s += '<br/><br/>' 
    return response


def transactions_stats(transactions):
    transactions = pd.DataFrame(transactions)
    counterParty_count = transactions['counterPartyName'].value_counts()
    t_s = transactions.groupby('counterPartyName').agg({'counterPartyName':len, 'amount':sum})
    
    s = ""
    for i in counterParty_count.index:
        s += str(i) + ": " + str(counterParty_count[i]) + "<br/>"
    #print(transactions)
    return s