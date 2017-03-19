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
	# if 'ppp' not in flask.session:
	# 	flask.session['ppp'] = (pd.read_csv('PPP.csv', sep=',', delimiter = ',', index_col = 'Country')).to_dict()['Rate']
	if 'sum_adj_cost' not in flask.session:
		flask.session['sum_adj_cost'] = 0
		flask.session['sum_duration'] = 0
	return redirect('http://127.0.0.1:8080/')


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
    return redirect('/')


#@app.route('/api/deutsche/transactions')
@app.route('/api/deutsche/transactions/<country>/<fr>/<to>')
def deutsche_transactions(country, fr, to):
	fr = datetime.date(int(fr[0:4]), int(fr[4:6]), int(fr[6:8]))
	to = datetime.date(int(to[0:4]), int(to[4:6]), int(to[6:8]))
	duration = to - fr
	duration = duration.days
	transactions = db.get_transactions(flask.session['db_token'])
	s = 0
	selected_transactions = {'transactions':[], 'sum':0}
	for t in transactions:
		d = datetime.date(int(t['bookingDate'][0:4]), int(t['bookingDate'][5:7]), int(t['bookingDate'][8:10]))
		if (fr is None or ((d >= fr) and (d <= to))) and (t['amount'] < 0):
			s += t['amount']
			selected_transactions['transactions'].append(t)
	selected_transactions['sum'] = round(s,0)
	selected_transactions['duration'] = duration
	selected_transactions['fr'] = fr
	selected_transactions['to'] = to
	selected_transactions['country'] = country	
	coef = (pd.read_csv('PPP.csv', sep=',', delimiter = ',', index_col = 'Country')).to_dict()['Rate'][country]
	selected_transactions['adj_sum'] = selected_transactions['sum']/coef
	if 'sum_adj_cost' not in flask.session:
		flask.session['sum_adj_cost'] = 0
		flask.session['sum_duration'] = 0
	flask.session['sum_adj_cost'] += selected_transactions['adj_sum']
	flask.session['sum_duration'] += selected_transactions['duration']
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


@app.route('/api/get_trip_cost/<country>/<fr>/<to>')
def get_trip_cost(country, fr, to):
	to_date = datetime.date(int(to[0:4]), int(to[4:6]), int(to[6:8]))
	fr_date = datetime.date(int(fr[0:4]), int(fr[4:6]), int(fr[6:8]))

	duration = to_date - fr_date
	duration = duration.days

	if to_date < datetime.date.today():
		t = deutsche_transactions(country, fr, to)
	else:
		coef = (pd.read_csv('PPP.csv', sep=',', delimiter = ',', index_col = 'Country')).to_dict()['Rate'][country]
		avg_adj_cost_day = flask.session['sum_adj_cost']/flask.session['sum_duration']
		cost_day = avg_adj_cost_day*coef
		total_cost = cost_day * duration
		t = jsonify({'sum' : round(total_cost,0),
			'duration' : duration,
			'fr' : fr_date,
			'to' : to_date,
			'country' : country})
		t.headers.add('Access-Control-Allow-Origin', '*')
	return t


if __name__ == "__main__":
    app.run()


