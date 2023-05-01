import adafruit_servokit

def main():
    print("Servo Menu")

    while True:
        print("Select a servo:")
        print("1 --> Arm Joint 1")
        print("2 --> Arm Joint 2")
        print("3 --> Arm Joint 3")
        print("G --> Gripper")
        selection = input("Selection: ")
        
        if selection == "":
            break
        elif selection == "1":
            angle = int(input("Joint 1 angle: "))
            
        elif selection == "2":
            angle = int(input("Joint 2 angle: "))
            
        elif selection == "3":
            angle = int(input("Joint 3 angle: "))
            
        elif selection == "G" or selection == "g":
            inches = float(input("Gripper distance: "))
        
        else:
            print("Invalid selection")

main()
