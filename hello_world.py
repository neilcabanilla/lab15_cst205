# hello_flask.py
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap5
from PIL import Image
import random


# create an instance of Flask
app = Flask(__name__)

# create instance of bootstrap
bootstrap = Bootstrap5(app)


# Task 2 for Lab 15
# route decorator binds a function to a URL
@app.route('/')
def hello():
  return '<h1>Hello world from Flask!</h1> <p> Neil: Extravagant </p>'

# Task 3 for Lab 15
# Template
@app.route('/neil')
def test():
  return render_template('my_template.html')

# Task 3 for Lab 16
my_dict = {'GameOne' : 'SuperMario', 'GameTwo' : 'DonkeyKong'}

@app.route('/dict')
def testtwo():
  return render_template('my_templatetwo.html', my_dict = my_dict)

# Task 4 for Lab 16
@app.route('/random')
def testthree():
  img_one = Image.open('static/game.jpeg')
  img_two = Image.open('static/gametwo.jpg')
  img_three = Image.open('static/gamethree.jpg')

  img_list = [img_one, img_two, img_three]

  ran_image = random.choice(img_list)
  neg_pixels = [(255 -p[0], 255 - p[1], 255 -p[2]) for p in ran_image.getdata()]

  neg_img = Image.new('RGB', ran_image.size)

  neg_img.putdata(neg_pixels)
  neg_img.save('static/testingneg.png')
  return render_template('my_templatethree.html')
'''
Github Link: https://github.com/neilcabanilla/lab15_cst205
'''