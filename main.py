from flask import Flask, jsonify
import requests
import os
os.system("pip install scratchattach")
import scratchattach as scratch3

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
import time
popular = [
    404041613, #among us jester mod server 1
    404013306, #among us jm s2
    441054306, #among us jester mod s3
    523967150, #amogus s1
    432072522, #amogus s2
    524390839, #amogus s2
    409593079, #othello
    417818985, #connect4 
    413527196, #chess
    12785898, #cpmf1
    378507713, #cpmf2
    108566337, #slither.io1
    544213416, #slither.io2
    702543294, #slither.io3
]
data = {}
for i in popular:
    data[i] = []


def get_user_list(projectid):
    try:
        logs = scratch3.get_cloud_logs(projectid)
        users = []
        for i in logs:
            if i["user"] not in users:
                users.append(i["user"])
    except Exception as e:
        print(e)
    return users
    
def sensor():
    
    global data
    for i in popular:
        data[i] = len(get_user_list(i))
    print(data)

app = Flask('app')
page_html = ""


@app.route('/')
def hello_world():
    return jsonify({"status":"up"})


@app.route('/api/')
def api():
    return data

app.run(host='0.0.0.0', port=8080)
