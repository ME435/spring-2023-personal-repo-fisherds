import time
import serial

def print_replies(ser):
    time.sleep(0.1)
    while (ser.in_waiting > 0):
        received = ser.readline()
        print("Received --> " + received.decode().strip())
        time.sleep(0.1)

def wait_for_reply(ser):
    while (ser.in_waiting == 0):
        time.sleep(0.1) # Done to avoid the ser.readline timeout
    received = ser.readline()
    print("Received --> " + received.decode().strip())

def open_serial_port(name="/dev/ttyS0"):
    ser = serial.Serial(name, baudrate = 19200)
    print("Connected")
    ser.reset_input_buffer()
    time.sleep(2.0)
    return ser

def main():
    ser = open_serial_port("/dev/tty.usbmodem11301")

    counter = 0
    while True:
        counter += 1
        message_bytes = b'Write counter: %d\n' % (counter)
        print(f"Sent     --> {message_bytes.decode().strip()}")
        ser.write(message_bytes)
        print_replies(ser)

        time.sleep(3)

main()