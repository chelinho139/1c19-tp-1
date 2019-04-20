from flask import Flask, send_from_directory
import requests
import time

app = Flask(__name__, static_url_path='')

HOST = '0.0.0.0'
PORT = 4000

SLEEP_TIME_IN_SECONDS = 2
INTENSIVE_COUNTER = 2000


def intensive_op(foo):
  print("foo {}".format(foo))
  foo = foo + 1
  return foo*foo


#CASE 1
@app.route("/", methods=["GET"])
def healt_check():
  return 'Doritos Dev - Python Test Server'

#CASE 1-bis
@app.route("/ping", methods=["GET"])
def ping():
  return 'OK'


#CASE 2
@app.route("/timeout", methods=["GET"])
def time_out():
  print("GET /timeout")
  time.sleep(SLEEP_TIME_IN_SECONDS)
  return "OK"


#CASE 3
@app.route("/intensive", methods=["GET"])
def intensive():
  print("GET /intensive")
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
    old_time = new_time
  return "OK"


#CASE 4
@app.route("/static", methods=["GET"])
def return_static_file():
  print("GET /static")
  return send_from_directory("static", "doritos.jpg")



#CASE 5
@app.route("/proxy", methods=["GET"])
def proxy():
  print("GET /proxy")
  url = 'http://'+HOST+':'+str(PORT)+'/timeout'
  res = requests.get(url)
  if res.status_code == 200:
    return "OK"
  return "NOT OK"



if __name__ == "__main__":
  app.run(host=HOST, port=PORT)

