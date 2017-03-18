import urllib
from flask import abort, request, Flask, redirect
import requests
import json
import pandas as pd
from services import api_deutsche as db

app = Flask(__name__)

# Authorization
@app.route("/")
def homepage():
    return redirect(db.make_authorization_url())

@app.route('/callback')
def deutsche_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    code = request.args.get('code')
    access_token = db.get_token(code)
    return db.transactions_stats(db.get_transactions(access_token))


@app.route('/api/countries')
def get_countries():
    countries = json.load(open('countriesToCities.json'))
    return 'o'

if __name__ == "__main__":
    app.run()