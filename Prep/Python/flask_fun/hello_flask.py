from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello, {name}!'

@app.route('/api/<command>')
def api_command(command):
    return send_command(command)

