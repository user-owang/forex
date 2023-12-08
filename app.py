from flask import *
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'er548o0nkjdfg'

@app.route('/')
def showHome():
  return render_template('home.html')

@app.route('/submit')
def checkRates():
  access_key = '30cd3ecc142ff4fcdb37b677be093e2f'
  source = request.args['source']
  currencies = request.args['currencies']
  amount = request.args['amount']
  res = requests.get('http://api.exchangerate.host/live', params={'access_key': access_key, 'source': source, 'currencies': currencies})
  if not res.json()['success']:
    if res.json().get('error').get('code') == 201:
      flash(f'Not a valid currency code: {source}')
    if res.json().get('error').get('code') == 202:
      flash(f'Not a valid currency code: {currencies}')
  return 'not true'
  