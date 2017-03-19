import urllib
from flask import abort, request, Flask, redirect, jsonify, Session, session
import flask
import requests
import json
import pandas as pd
from services import api_deutsche as db, api_instagram as inst, api_flickr as flickr
import datetime

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'


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


@app.route('/clear_session')
def clear_session():
	session.clear()
	return redirect('/')


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

# @app.route('/api/deutsche/transactions')
# def deutsche_transactions():
# 	return jsonify(db.get_transactions(flask.session['db_token']))

@app.route('/api/deutsche/transactions')
@app.route('/api/deutsche/transactions/<fr>/<to>')
def deutsche_transactions(fr = None, to = None):
	if fr is not None:
		fr = datetime.date(int(fr[0:4]), int(fr[4:6]), int(fr[6:8]))
		to = datetime.date(int(to[0:4]), int(to[4:6]), int(to[6:8]))
	transactions = db.get_transactions(flask.session['db_token'])
	s = 0
	selected_transactions = {'transactions':[], 'sum':0}
	for t in transactions:
		d = datetime.date(int(t['bookingDate'][0:4]), int(t['bookingDate'][5:7]), int(t['bookingDate'][8:10]))
		if (fr is None or ((d >= fr) and (d <= to))) and (t['amount'] < 0):
			s += t['amount']
			selected_transactions['transactions'].append(t)
	selected_transactions['sum'] = s
	resp = jsonify(selected_transactions)
	resp.headers.add('Access-Control-Allow-Origin', '*')
	return resp


# get list of countries
@app.route('/api/countries')
def get_countries():
    countries = json.load(open('countriesToCities.json'))
    resp = jsonify(sorted(list(countries.keys())))
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


@app.route('/api/status')
def get_apistatus():
	s = {}
	if 'db_token' in flask.session:
		s['deutsche_status'] = True
	else:
		s['deutsche_status'] = False
	if 'inst_token' in flask.session:
		s['instagram_status'] = True
		s['instagram_username'] = flask.session['inst_username']
	else:
		s['instagram_status'] = False
	resp = jsonify(s)
	resp.headers.add('Access-Control-Allow-Origin', '*')
	return resp

# get JSON of user's photos in the selected period
@app.route('/api/instagram/photos/<fr>/<to>')
def inst_get_photos(fr, to):
	fr = datetime.date(int(fr[0:4]), int(fr[4:6]), int(fr[6:8]))
	to = datetime.date(int(to[0:4]), int(to[4:6]), int(to[6:8]))
	p = inst.get_photos(flask.session['inst_userid'], flask.session['inst_token'], fr, to)
	resp = jsonify(p)
	resp.headers.add('Access-Control-Allow-Origin', '*')
	return resp

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


@app.route('/api/flickr/photos/<country>/<season>/')
def flickr_get_photos(country, season):
	p = flickr.get_images(country, season, 5)
	resp = jsonify(p)
	resp.headers.add('Access-Control-Allow-Origin', '*')
	return resp

@app.route('/api/get_photos_any/<country>/<fr>/<to>')
def get_photos_any(country, fr, to):
	to_date = datetime.date(int(to[0:4]), int(to[4:6]), int(to[6:8]))
	
	if to_date < datetime.date.today():
		return inst_get_photos(fr, to)
	else:
		month_from = int(fr[4:6])
		season = 'Winter'
		if month_from in [3,4,5]:
			season = 'Spring'
		elif month_from in [6,7,8]:
			season = 'Summer'
		elif month_from in [9,10,11]:
			season = 'Fall'
		return flickr_get_photos(country, season)

if __name__ == "__main__":
    app.run()


