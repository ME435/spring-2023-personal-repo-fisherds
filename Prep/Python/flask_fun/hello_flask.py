from flask import Flask
from flask import render_template

app = Flask(__name__)

def send_command(command):
    print("Server side", command)
    return "READY" + " cmd: " + command

@app.route('/')
def hello():
    # return 'Hello World!'
    return render_template("index.html")

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello, {name}!'

@app.route('/api/<command>')
def api_command(command):
    return send_command(command)
