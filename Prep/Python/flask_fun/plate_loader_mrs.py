import time
import serial

from flask import Flask
from flask import render_template

def send_message(ser, command):
    message_bytes = (command + "\n").encode()
    print(f"Sent     --> {message_bytes.decode().strip()}")
    ser.write(message_bytes)
    return wait_for_reply(ser)

def wait_for_reply(ser):
    while ser.in_waiting == 0:
        time.sleep(0.1) # Done to avoid the ser.readline timeout
    while ser.in_waiting > 0:
        received = ser.readline()
        try:
            print("Received --> " + received.decode().strip())
        except:
            print("An exception occurred")
    return received


def open_serial_port(name="/dev/ttyS0"):
    ser = serial.Serial(name, baudrate = 19200)
    print("Connected")
    time.sleep(2.0)
    ser.reset_input_buffer()
    return ser


app = Flask(__name__)
# ser = open_serial_port("/dev/tty.usbmodem1101")
ser = open_serial_port("/dev/tty.usbserial-210")

@app.route('/')
def hello():
    # return 'Hello World!'
    return render_template("index.html")

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello, {name}!'

@app.route('/api/<command>')
def api_command(command):
    # print(f"Got the request {command}")
    # return f"Got {command}"
    return send_message(ser, command)

