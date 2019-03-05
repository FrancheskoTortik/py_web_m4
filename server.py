from bottle import route, run, view, get, static_file
from datetime import datetime as dt
from random import random
import os
import horoscope

cwd = os.getcwd() + os.sep + 'views' + os.sep + 'predictions.tpl'

@route("/")
@view(cwd)
def index():
  now = dt.now()

  x = random()

  return {
    "date": f"{now.year}-{now.month}-{now.day}",
    "predictions": horoscope.generate_prophecies(),
    "special_date": x > 0.5,
    "x": x,
  }

@route("/api/test")
def api_test():
    return {"test_passed": True}

@route("/api/new")
def api_new ():
    return {"prophises" : horoscope.generate_prophecies()}  

@route('/helpers.js')
def js():
   return static_file('helpers.js', root='.')

run(
  host="localhost",
  port=8080,
  autoreload=True
)