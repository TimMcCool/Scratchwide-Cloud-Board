from flask import Flask, jsonify
import requests
import os
os.system("pip install scratchattach")
import scratchattach as scratch3
import time

def get_user_list(projectid):
    projectid = projectid.replace(" ", "")
    try:
        logs = scratch3.get_cloud_logs(projectid)
        users = []
        for i in logs:
            if i["user"] =! users:
                if not int(i['timestamp']) < round((time.time() - 10) * 1000):
                    users.append(i["user"])
    except Exception as e:
        print(e)
    return users

        
session = scratch3.Session(os.environ["sessionid"], username="TimMcCool") #replace with your data
conn = session.connect_cloud(project_id="417579977") #replace with your project id

client = scratch3.CloudRequests(conn) #optional argument: ignore_exceptions=True

@client.request
def popular():
    data = requests.get("https://scratchwide-cloud-board-popular-projects.1tim.repl.co/api/").json()
    response = []
    for item in data:
        
        response.append(item)
        response.append(data[item])
    return response

@client.request
def project(projectid):
    try:
        name = scratch3.get_project(projectid).title
        if len(name) > 35:
            name = name[:32]+"..."
    except Exception:
        name = "Unknown (Unshared project)"
    try:
        players = get_user_list(projectid)
    except Exception:
        players = ["Invalid project id!"]
        name = "None"
    if len(players) == 0:
        players = ["No one is playing this game right now!"]
    return [name] + players
    
@client.event
def on_ready():
    print("Request handler is ready")


app = Flask('app')
page_html = ""

        
@app.route('/')
def hello_world():
    return jsonify({"status":"up"})

def keep_alive():
    app.run(host='0.0.0.0', port=8080)

from threading import Thread
thread = Thread(target=keep_alive, args=())
thread.start()

client.run()
