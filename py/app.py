from flask import Flask, send_from_directory
import requests
import time

app = Flask(__name__, static_url_path='')


SLEEP_TIME_IN_SECONDS = 2
INTENSIVE_COUNTER = 2000


def intensive_op(foo):
  print("foo {}".format(foo))
  foo = foo + 1
  return foo*foo


#CASE 1
@app.route("/", methods=["GET"])
def healt_check():
  return 'Doritos Dev - Node Test Server'

#CASE 2
@app.route("/timeout", methods=["GET"])
def time_out():
  time.sleep(SLEEP_TIME_IN_SECONDS)
  return "OK"


#CASE 3
@app.route("/intensive", methods=["GET"])
def intensive():
  old_time = time.time()
  delta = 0
  foo = 0
  counter = 0
  while counter < INTENSIVE_COUNTER:
    #do anything calculate
    intensive_op(foo)
    new_time = time.time()
    delta = new_time - old_time
    print("delta {}".format(counter))
    counter = counter + delta
    print("counter {}".format(counter))
    oldTime = new_time
  return "OK"


#CASE 4
@app.route("/static", methods=["GET"])
def return_static_file():
  return send_from_directory("static", "doritos.jpg")



#CASE 5
@app.route("/proxy", methods=["GET"])
def proxy():
  print("GET /timeout")
  res = requests.get("http://localhost:5000/timeout")
  if res.status_code == 200:
    return "OK"
  return "NOT OK"


app.run()



