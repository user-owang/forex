from flask import *
from checkresponses import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'er548o0nkjdfg'

@app.route('/')
def showHome():
  return render_template('home.html')

@app.route('/submit')
def checkRates():
  source = request.args['source']
  currencies = request.args['currencies']
  amount = request.args['amount']
  is_valid = validate_form(source,currencies,amount)
  if is_valid['valid']:
    rate = float(is_valid['results']['quotes'][source+currencies])
    return render_template('results.html', rate = rate, amount = float(amount), source = source, currencies = currencies)
  else:
    if is_valid['results']['errors'].count('error_cur'):
      for term in is_valid['results']['errors']:
        flash(f'Not a valid code: {term}')
    if is_valid['results']['errors'].count('error_amt'):
      flash('Not a valid amount')
  return redirect('/')