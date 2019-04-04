from flask import Flask,send_from_directory
import requests
import time
import datetime

app = Flask(__name__, static_url_path='static')


SLEEP_TIME = 2000


def intensive_op(foo):
  foo = foo + 1
  return foo*foo


#CASE 1
@app.route("/",methods=["GET"])
def healt_check():
  return 'Doritos Dev - Node Test Server'

#CASE 2
@app.route("/timeout",methods=["GET"])
def time_out():
  time.sleep(SLEEP_TIME)
  return "OK"


#CASE 3
@app.route("/intensive",methods=["GET"])
def intensive():
  old_time = datetime.datetime.now()
  delta = 0
  foo = 0
  counter = 0
  while counter < SLEEP_TIME:
    intensive_op(foo)
    new_time = datetime.datetime.now()
    delta = new_time.date() - old_time.date()
    counter = counter + delta
    oldTime = new_time
  return "OK"


#CASE 4
@app.route("/static",methods=["GET"])
def return_static_file():
  return send_from_directory("doritos.jpg")



#CASE 5
@app.route("/proxy",methods=["GET"])
def proxy():
  print("GET /timeout")
  res = requests.get("http:localhost:4000/timeout")
  if res.status_code == 200:
    return "OK"
  return "NOT OK"



