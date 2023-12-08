### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  - in python you dont have to declare variables
  - variables are named using snake case typically
  - there are no constants in python
  - javascript can return undefined and continue running, whereas python will error out
  - different equity operators in javascript and python
  - you can import other packages in python
- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.
  - you could use list.get('c')
  - you could use a try and except to catch the error and return something else
- What is a unit test?
  - a unit test is a test to see if one specific function is working correctly
- What is an integration test?
  - an integration test is used to see if a group of functions is working together correctly to accomplish a goal
- What is the role of web application framework, like Flask?
  - Flask is used to manage the back end of a web application
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  - if the topic of the page is about pretzels, you would likely use it as a parameter in the route URL, but if pretzels are used to modify an existing page, using it as a query parameter makes more sense.
- How do you collect data from a URL placeholder parameter using Flask?
  - in the route URL, you would use <placeholder> for the parameter. It is then passed through as an argument in the view function to be referenced inside.
- How do you collect data from the query string using Flask?
  - you would use request.args('querystring')
- How do you collect data from the body of the request using Flask?
  - request.data
- What is a cookie and what kinds of things are they commonly used for?
  - a cookie is a string that is saved on the client side and is sent with every request. They are commonly used to keep track of logged in users or shopping carts
- What is the session object in Flask?
  - it is a dictionary object that stores information in key-value pairs and is encrypted and sent as a cookie to be stored client side.
- What does Flask's `jsonify()` do?
  - it converts code into JSON accessible data
