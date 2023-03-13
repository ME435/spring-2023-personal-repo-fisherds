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
    ser = open_serial_port("/dev/tty.usbmodem1101")
    while True:
        print("1: Reset")
        print("2: X-Axis")
        print("3: Z-Axis")
        print("4: Gripper")
        print("5: Move")
        print("6: Loader Status")
        choice = input("Make a selection: ")
        if choice == "" or choice == "0":
            break
        if choice == "1":
            send_message(ser, "RESET")
        if choice == "2":
            arg = input("Where to: ")
            send_message(ser, f"X-AXIS {arg}")
        if choice == "3":
            arg = input("Press e to Extend, r to Retract: ")
            if arg == "e":
                send_message(ser, "Z-AXIS EXTEND")
            if arg == "r":
                send_message(ser, "Z-AXIS RETRACT")
        if choice == "4":
            arg = input("Press o to Open, c to Close: ")
            if arg == "o":
                send_message(ser, "GRIPPER OPEN")
            if arg == "c":
                send_message(ser, "GRIPPER CLOSE")
        if choice == "5":
            arg1 = input("Plate start: ")
            arg2 = input("Plate finish: ")
            send_message(ser, f"MOVE {arg1} {arg2}")
        if choice == "6":
            send_message(ser, "LOADER_STATUS")

    print("Goodbye")

main()
