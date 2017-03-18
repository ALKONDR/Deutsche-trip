import urllib
from flask import abort, request, Flask, redirect, jsonify, Session
import flask
import requests
import json
import pandas as pd
from services import api_deutsche as db, api_instagram as inst

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
sess = Session()


@app.route('/')
def homepage():
	s = "<a href = '/api/deutsche'>auth deutshce</a> <br/> <a href = '/api/instagram'>auth inst</a> "
	s += '<br/><br/>'

	s += 'Deutsche bank authorization status: '
	if 'db_token' in flask.session:
	 	s += 'OK'
	else:
		s += '-'
	s += '<br/>'

	s += 'Instagram authorization: '
	if 'inst_userid' in flask.session:
		s += flask.session['inst_username']
	else: 
		s += '-'
	return s


# Authorization
@app.route("/api/deutsche")
def deutsche_auth():
    return redirect(db.make_authorization_url())

@app.route('/api/deutsche/callback')
def deutsche_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    code = request.args.get('code')
    db_token = db.get_token(code)
    if 'db_token' not in flask.session:
    	flask.session['db_token'] = db_token
    #print db.transactions_stats(db.get_transactions(access_token))
    return redirect('/')

# get list of countries
@app.route('/api/countries')
def get_countries():
    countries = json.load(open('countriesToCities.json'))
    return jsonify(sorted(list(countries.keys())))


@app.route('/api/instagram')
def inst_auth():
	return redirect(inst.make_authorization_url())

@app.route('/api/instagram/callback')
def inst_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    code = request.args.get('code')
    if 'inst_userid' not in flask.session:
    	flask.session['inst_token'], flask.session['inst_userid'], flask.session['inst_username']  = inst.get_token(code)
    #inst_token = inst.get_token(code)
    return redirect('/')


if __name__ == "__main__":
    app.run()


