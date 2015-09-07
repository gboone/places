from flask import Flask, render_template, request, session, g, redirect, \
    url_for, abort
import json
import os
import geocoder
import requests
from lib.foursquare import Foursquare

app = Flask(__name__)
app.debug = True
def authorize_user(code):
    client_id = os.environ['FSQID']
    secret = os.environ['FSQSECRET']
    params={
        "client_id":client_id,
        "client_secret":secret,
        "grant_type":"authorization_token",
        "redirect_uri":"http://127.0.0.1:5000/auth",
        "code":code
    }
    url = "https://foursquare.com/oauth2/access_token"
    token = requests.get(url, params=params)
    return token

@app.route("/", methods=["GET"])
def index():
    if os.environ['FSQTOKEN']:
        fsq = Foursquare(os.environ['FSQTOKEN'])
        checkins = fsq.checkins()
        return render_template('index.html', token=os.environ['FSQTOKEN'], checkins=checkins)

@app.route("/auth", methods=['GET'])
def auth():
    import pdb; pdb.set_trace()
    return render_template('index.html')

app.run()
