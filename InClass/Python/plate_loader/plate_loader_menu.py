def main():
    ser = "Fake Serial port object"

    while True:
        print("1: RESET")
        print("2: X-AXIS")
        print("3: Z-AXIS")
        print("4: GRIPPER")
        print("5: MOVE")
        print("6: LOADER_STATUS")
        selection = input("Selection: ")
        if selection == "0" or selection == "":
            break
        if selection == "1":
            send_command(ser, "RESET")
        if selection == "2":
            arg = input("Where to? ")
            send_command(ser, f"X-AXIS {arg}")
        if selection == "3":
            arg = input("Press e to Extend, or r to retract: ")
            if arg == "e":
                send_command(ser, "Z-AXIS EXTEND")
            if arg == "r":
                send_command(ser, "Z-AXIS RETRACT")
        if selection == "4":
            arg = input("Press o to Open, or c to Close: ")
            if arg == "o":
                send_command(ser, "GRIPPER OPEN")
            if arg == "c":
                send_command(ser, "GRIPPER CLOSE")
        if selection == "5":
            arg1 = input("Plate start: ")
            arg2 = input("Plate end:   ")
            send_command(ser, f"MOVE {arg1} {arg2}")
        if selection == "6":
            send_command(ser, "LOADER_STATUS")

def send_command(ser, command):
    print("TODO: send the command: ", command)

main()
