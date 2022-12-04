from flask import Flask, render_template, url_for
from flask_cors import CORS, cross_origin
import requests
import os

import socket
import time

HOSTNAME = socket.gethostname()

ips = {
    "instance-from-template-a": os.getenv('INSTANCE_A_ADRESS'),
    "instance-from-template-b": os.getenv('INSTANCE_B_ADRESS'),
    "instance-from-template-c": os.getenv('INSTANCE_C_ADRESS')
}

next = {
    "instance-from-template-a": "instance-from-template-b",
    "instance-from-template-b": "instance-from-template-c",
    "instance-from-template-c": "instance-from-template-a"
}

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.token = False
if HOSTNAME == "instance-from-template-a":
    app.token = True

@app.route("/")
def index():
    return render_template(
        'index.html', 
        check_token_url=f"\'{url_for('check_token')}\'",
        send_token_url=f"\'{url_for('send_token')}\'",
        hostname=f"\'HOSTNAME\'",
        button_string=f"\'Send token to {next[HOSTNAME]}\'"
        )

@app.route("/check_token")
def check_token():
    return "", 200 if app.token else 401

@app.route("/receive_token")
def receive_token():
    app.token = True
    return ""

@app.route("/send_token")
def send_token():
    if not app.token:
        return "", 401
    url = f"http://{next[HOSTNAME]/receive_token}"
    requests.get(url)
    return "", 200
