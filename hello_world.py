# hello_flask.py
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap5


# create an instance of Flask
app = Flask(__name__)

# create instance of bootstrap
bootstrap = Bootstrap5(app)


# Task 2
# route decorator binds a function to a URL
@app.route('/')
def hello():
  return '<h1>Hello world from Flask!</h1> <p> Neil: Extravagant </p>'

# Task 3
# Template
@app.route('/neil')
def test():
  return render_template('my_template.html')
