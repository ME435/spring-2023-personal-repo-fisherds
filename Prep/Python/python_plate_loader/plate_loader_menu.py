import time
import serial

def send_message(ser, command):
    message_bytes = (command + "\n").encode()
    print(f"Sent     --> {message_bytes.decode().strip()}")
    ser.write(message_bytes)
    wait_for_reply(ser)

def print_replies(ser):
    time.sleep(0.1)
    while ser.in_waiting > 0:
        received = ser.readline()
        print("Received --> " + received.decode().strip())
        time.sleep(0.1)

def wait_for_reply(ser):
    while ser.in_waiting == 0:
        time.sleep(0.1) # Done to avoid the ser.readline timeout
    received = ser.readline()
    print("Received --> " + received.decode().strip())

def open_serial_port(name="/dev/ttyS0"):
    ser = serial.Serial(name, baudrate = 19200)
    print("Connected")
    time.sleep(2.0)
    ser.reset_input_buffer()
    return ser

def main():
    ser = open_serial_port("/dev/tty.usbmodem11301")
    while True:
        print("0: Exit")
        print("1: Reset")
        print("2: X-aix")
        print("3: Z-axis")
        print("4: Gripper")
        choice = input("Make a selection: ")
        if choice == "0":
            break
        if choice == "1":
            send_message(ser, "RESET")
        if choice == "2":
            to_pos = input("Where to: ")
            send_message(ser, f"X-AXIS {to_pos}")
        if choice == "3":
            bowens_var = input("Press 1 to Extend, 2 to Retract: ")
            if bowens_var == "1":
                message_bytes = b'Z-AXIS EXTEND\n'
                print(f"Sent     --> {message_bytes.decode().strip()}")
                ser.write(message_bytes)
            if bowens_var == "2":
                message_bytes = b'Z-AXIS RETRACT\n'
                print(f"Sent     --> {message_bytes.decode().strip()}")
                ser.write(message_bytes)
            wait_for_reply(ser)

    print("Goodbye")

main()
