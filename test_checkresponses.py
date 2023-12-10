from checkresponses import *
from unittest import TestCase

class CheckResponsesTests(TestCase):
  def checkAllInvalid(self):
    all_invalid = validate_form('asdf1','asdf2','asdf')
    
    self.assertIsInstance(all_invalid, dict)
    self.assertFalse(all_invalid['valid'])
    self.assertEqual(len(all_invalid['results']['errors']), 2)
    self.assertEqual(len(all_invalid['results']['inputs']), 2)
    self.assertIn('asdf1', all_invalid['results'['inputs']])
    self.assertIn('asdf2', all_invalid['results'['inputs']])
    self.assertIn('error_cur', all_invalid['results'['errors']])
    self.assertIn('error_amt', all_invalid['results'['errors']])
  
  def checkSourceInvalid(self):
    source_invalid = validate_form('asdf1','USD','10')

    self.assertIsInstance(source_invalid, dict)
    self.assertFalse(source_invalid['valid'])
    self.assertEqual(len(source_invalid['results']['errors']), 1)
    self.assertEqual(len(source_invalid['results']['inputs']), 1)
    self.assertIn('error_cur', source_invalid['results']['errors'])
    self.assertIn('asdf1', source_invalid['results']['inputs'])

  def checkCurrenciesInvalid(self):
    currencies_invalid = validate_form('EUR','asdf2','10')

    self.assertIsInstance(currencies_invalid, dict)
    self.assertFalse(currencies_invalid['valid'])
    self.assertEqual(len(currencies_invalid['results']['errors']), 1)
    self.assertEqual(len(currencies_invalid['results']['inputs']), 1)
    self.assertIn('error_cur', currencies_invalid['results']['errors'])
    self.assertIn('asdf2', currencies_invalid['results']['inputs'])

  def checkAmountInvalid(self):
    amount_invalid = validate_form('EUR','USD','asdf')

    self.assertIsInstance(amount_invalid, dict)
    self.assertFalse(amount_invalid['valid'])
    self.assertEqual(len(amount_invalid['results']['errors']), 1)
    self.assertEqual(len(amount_invalid['results']['inputs']), 0)
    self.assertIn('error_amt', amount_invalid['results']['errors'])

  def checkSourceAmountInvalid(self):
    SA_invalid = validate_form('asdf1','USD','asdf')

    self.assertIsInstance(SA_invalid, dict)
    self.assertFalse(SA_invalid['valid'])
    self.assertEqual(len(SA_invalid['results']['errors']), 2)
    self.assertEqual(len(SA_invalid['results']['inputs']), 1)
    self.assertIn('error_amt', SA_invalid['results']['errors'])
    self.assertIn('error_cur', SA_invalid['results']['errors'])
    self.assertIn('asdf1', SA_invalid['results']['inputs'])

  def checkSourceCurrenciesInvalid(self):
    SC_invalid = validate_form('asdf1','asdf2','10')

    self.assertIsInstance(SC_invalid, dict)
    self.assertFalse(SC_invalid['valid'])
    self.assertEqual(len(SC_invalid['results']['errors']), 1)
    self.assertEqual(len(SC_invalid['results']['inputs']), 2)
    self.assertIn('error_cur', SC_invalid['results']['errors'])
    self.assertIn('asdf2', SC_invalid['results']['inputs'])
    self.assertIn('asdf1', SC_invalid['results']['inputs'])

  def checkCurrenciesAmountInvalid(self):
    CA_invalid = validate_form('EUR','asdf2','asdf')

    self.assertIsInstance(CA_invalid, dict)
    self.assertFalse(CA_invalid['valid'])
    self.assertEqual(len(CA_invalid['results']['errors']), 2)
    self.assertEqual(len(CA_invalid['results']['inputs']), 1)
    self.assertIn('error_amt', CA_invalid['results']['errors'])
    self.assertIn('error_cur', CA_invalid['results']['errors'])
    self.assertIn('asdf2', CA_invalid['results']['inputs'])

  def checkValid(self):
    all_valid = validate_form('EUR','USD','10')

    self.assertIsInstance(all_valid, dict)
    self.assertTrue(all_valid['valid'])
    self.assertTrue(all_valid['results']['success'])
    self.assertEqual(all_valid['results']['source'], 'EUR')
    self.assertIn('EURUSD',all_valid['results']['quotes'])