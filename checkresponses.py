import requests

access_key = '30cd3ecc142ff4fcdb37b677be093e2f'
list = requests.get('http://api.exchangerate.host/list', params={'access_key': access_key})
valid_cur = set(list.json()['currencies'].keys())

def validate_form(source,currencies,amount):
  """outputs a list containing T/F for any invalid inputs, what kind of value error, and what input the error occurred in."""
  answer = {'valid': True}

  try:
    new_amount = float(amount)
  except:
    new_amount = amount
  finally:
    if source in valid_cur and currencies in valid_cur and isinstance(new_amount, float):
      res = requests.get('http://api.exchangerate.host/live', params={'access_key': access_key, 'source': source, 'currencies': currencies})
      answer['results']= res.json()
    
    else:
      answer['valid'] = False
      errors = []
      inputs = []
      if source not in valid_cur:
        inputs.append(source)
        errors.append('error_cur')
      if currencies not in valid_cur:
        inputs.append(currencies)
        if 'error_cur' not in errors:
          errors.append('error_cur')
      if not isinstance(new_amount, float):
        errors.append('error_amt')
      answer['results'] = {'errors': errors, 'inputs': inputs}
    
    return answer