from unittest import TestCase
from app import app

class AppTests(TestCase):
  def test_checkHome(self):
    """checks home page is loading correctly"""
    with app.test_client() as client:
      resp = client.get('/')
      html = resp.get_data(as_text = True)

      self.assertEqual(resp.status_code, 200)
      self.assertIn('<h1>Forex Converter</h1>', html)

  def test_checkSubmitAllInvalidRedirect(self):
    """checks that submit with all inputs invalid is redirecting back to home"""
    with app.test_client() as client:
      resp = client.get('/submit?source=asdf1&currencies=asdf2&amount=asdf')

      self.assertEqual(resp.status_code, 302)
      self.assertEqual(resp.location, 'http://localhost/')

  def test_checkSubmitAllInvalidRedirectFollowedAndFlashed(self):
    """checks that submit with all inputs invalid is redirecting back to home and the page is loading correctly with all flashed error messages showing"""
    with app.test_client() as client:
      resp = client.get('/submit?source=asdf1&currencies=asdf2&amount=asdf', follow_redirects=True)
      html = resp.get_data(as_text=True)

      self.assertEqual(resp.status_code, 200)
      self.assertIn('<div class="error">Not a valid code: asdf1</div>', html)
      self.assertIn('<div class="error">Not a valid code: asdf2</div>', html)
      self.assertIn('<div class="error">Not a valid amount</div>', html)
  
  def test_checkSubmitSourceInvalidRedirect(self):
    """checks that submit with only source input invalid is redicrecting back to home"""
    with app.test_client() as client:
      resp = client.get('/submit?source=asdf1&currencies=USD&amount=100')

      self.assertEqual(resp.status_code, 302)
      self.assertEqual(resp.location, 'http://localhost/')

  def test_checkSubmitSourceInvalidRedirectFollowedAndFlashed(self):
    """checks that submit with only source input invalid is redirecting back to home and the page is loading correctly with only one flashed error message showing"""
    with app.test_client() as client:
      resp = client.get('/submit?source=asdf1&currencies=USD&amount=100', follow_redirects=True)
      html = resp.get_data(as_text=True)

      self.assertEqual(resp.status_code, 200)
      self.assertIn('<div class="error">Not a valid code: asdf1</div>', html)
      self.assertNotIn('<div class="error">Not a valid code: USD</div>', html)
      self.assertNotIn('<div class="error">Not a valid amount</div>', html)
      
  def test_checkSubmitCurrenciesInvalidRedirect(self):
    """checks that submit with only currencies input invalid is redicrecting back to home"""
    with app.test_client() as client:
      resp = client.get('/submit?source=USD&currencies=asdf2&amount=100')

      self.assertEqual(resp.status_code, 302)
      self.assertEqual(resp.location, 'http://localhost/')

  def test_checkSubmitCurrenciesInvalidRedirectFollowedAndFlashed(self):
    """checks that submit with only currencies input invalid is redirecting back to home and the page is loading correctly with only one flashed error message showing"""
    with app.test_client() as client:
      resp = client.get('/submit?source=USD&currencies=asdf2&amount=100', follow_redirects=True)
      html = resp.get_data(as_text=True)

      self.assertEqual(resp.status_code, 200)
      self.assertIn('<div class="error">Not a valid code: asdf2</div>', html)
      self.assertNotIn('<div class="error">Not a valid code: USD</div>', html)
      self.assertNotIn('<div class="error">Not a valid amount</div>', html)
  
  def test_checkSubmitAmountInvalidRedirect(self):
    """checks that submit with only amount input invalid is redicrecting back to home"""
    with app.test_client() as client:
      resp = client.get('/submit?source=EUR&currencies=USD&amount=asdf')

      self.assertEqual(resp.status_code, 302)
      self.assertEqual(resp.location, 'http://localhost/')

  def test_checkSubmitSourceInvalidRedirectFollowedAndFlashed(self):
    """checks that submit with only amount input invalid is redirecting back to home and the page is loading correctly with only one flashed error message showing"""
    with app.test_client() as client:
      resp = client.get('/submit?source=EUR&currencies=USD&amount=asdf', follow_redirects=True)
      html = resp.get_data(as_text=True)

      self.assertEqual(resp.status_code, 200)
      self.assertIn('<div class="error">Not a valid amount</div>', html)
      self.assertNotIn('<div class="error">Not a valid code: USD</div>', html)
      self.assertNotIn('<div class="error">Not a valid code: EUR</div>', html)

  def test_checkSubmitSourceCurrenciesInvalidRedirect(self):
    """checks that submit with source and currencies inputs invalid is redirecting back to home"""
    with app.test_client() as client:
      resp = client.get('/submit?source=asdf1&currencies=asdf2&amount=100')

      self.assertEqual(resp.status_code, 302)
      self.assertEqual(resp.location, 'http://localhost/')

  def test_checkSubmitSourceCurrenciesInvalidRedirectFollowedAndFlashed(self):
    """checks that submit with source and currencies inputs invalid is redirecting back to home and the page is loading correctly with all flashed error messages showing"""
    with app.test_client() as client:
      resp = client.get('/submit?source=asdf1&currencies=asdf2&amount=100', follow_redirects=True)
      html = resp.get_data(as_text=True)

      self.assertEqual(resp.status_code, 200)
      self.assertIn('<div class="error">Not a valid code: asdf1</div>', html)
      self.assertIn('<div class="error">Not a valid code: asdf2</div>', html)
      self.assertNotIn('<div class="error">Not a valid amount</div>', html)

  def test_checkSubmitSourceAmountInvalidRedirect(self):
    """checks that submit with source and amount inputs invalid is redirecting back to home"""
    with app.test_client() as client:
      resp = client.get('/submit?source=asdf1&currencies=USD&amount=asdf')

      self.assertEqual(resp.status_code, 302)
      self.assertEqual(resp.location, 'http://localhost/')

  def test_checkSubmitSourceAmountInvalidRedirectFollowedAndFlashed(self):
    """checks that submit with source and amount inputs invalid is redirecting back to home and the page is loading correctly with all flashed error messages showing"""
    with app.test_client() as client:
      resp = client.get('/submit?source=asdf1&currencies=USD&amount=asdf', follow_redirects=True)
      html = resp.get_data(as_text=True)

      self.assertEqual(resp.status_code, 200)
      self.assertIn('<div class="error">Not a valid code: asdf1</div>', html)
      self.assertNotIn('<div class="error">Not a valid code: USD</div>', html)
      self.assertIn('<div class="error">Not a valid amount</div>', html)

  def test_checkSubmitCurrenciesAmountInvalidRedirect(self):
    """checks that submit with currencies and amount inputs invalid is redirecting back to home"""
    with app.test_client() as client:
      resp = client.get('/submit?source=EUR&currencies=asdf2&amount=asdf')

      self.assertEqual(resp.status_code, 302)
      self.assertEqual(resp.location, 'http://localhost/')

  def test_checkSubmitCurrenciesAmountInvalidRedirectFollowedAndFlashed(self):
    """checks that submit with currencies and amount inputs invalid is redirecting back to home and the page is loading correctly with all flashed error messages showing"""
    with app.test_client() as client:
      resp = client.get('/submit?source=EUR&currencies=asdf2&amount=asdf', follow_redirects=True)
      html = resp.get_data(as_text=True)

      self.assertEqual(resp.status_code, 200)
      self.assertNotIn('<div class="error">Not a valid code: EUR</div>', html)
      self.assertIn('<div class="error">Not a valid code: asdf2</div>', html)
      self.assertIn('<div class="error">Not a valid amount</div>', html)
  
  def test_checkSubmitAllValidResults(self):
    """checks that submit with all inputs valid is rendering correct template"""
    with app.test_client() as client:
      resp = client.get('/submit?source=USD&currencies=USD&amount=10')
      html = resp.get_data(as_text=True)

      self.assertEqual(resp.status_code, 200)
      self.assertIn('10.0 USD converts to 10.0 USD', html)