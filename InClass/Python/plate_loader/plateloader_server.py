from flask import Flask
import serial
import time

app = Flask(__name__)


def send_command(ser, command):
    print("Sending: ", command)
    command = command + "\n"
    ser.write(command.encode())
    return wait_for_response(ser)


def wait_for_response(ser):
    while ser.in_waiting == 0:
        time.sleep(0.1)
    while ser.in_waiting > 0:
        response = ser.readline()
    print(f"Received --> {response}")
    return response


def open_serial(comPort="/dev/tty.usbmodem1101"):
    ser = serial.Serial(comPort, baudrate=19200)    
    while ser.is_open == False:
        time.sleep(0.1)
    
    # time.sleep(2)

    ser.flush()
    print("Connected")
    return ser

@app.route("/")
def hello_world():
    return "<p>Hello, Class!</p>"

@app.route("/name/<name>")
def hello_name(name):
    return f"<p>Hello, {name}!</p>"

@app.before_first_request
def initialize():
    print("Called only once, when the first request comes in")
    app.ser = open_serial()


@app.route("/api/<command>")
def plateloader_commands(command):
    reply = send_command(app.ser, command)
    return reply.decode().strip()



