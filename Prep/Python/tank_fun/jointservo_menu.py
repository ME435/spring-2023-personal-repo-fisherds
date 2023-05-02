"""
Authors:  Dave Fisher and PUT_YOUR_NAME_HERE.
"""
import time
import adafruit_servokit
from numpy import interp

def main():
    """ Test a robot's SERVOS. """
    print()
    print('--------------------------------------------------')
    print('Testing the  SERVOS  of a robot')
    print('--------------------------------------------------')

    # PIN_CAMERA_SERVO = 11
    PIN_JOINT_1 = 12
    PIN_JOINT_2 = 13
    PIN_JOINT_3 = 14
    PIN_GRIPPER_SERVO = 15

    servo_kit = adafruit_servokit.ServoKit(channels=16)

    while True:

        print("Type in a servo number.  Options:")
        print("1 --> Arm Joint 1")
        print("2 --> Arm Joint 2")
        print("3 --> Arm Joint 3")
        print("G --> Gripper")
        selection = input("Selection: ")
        if selection == "":
            break
        elif selection == "1":
            angle = int(input("Joint 1 angle: "))
            angle = interp(angle, [-90, 90], [180, 0])  # flip
            servo_kit.servo[PIN_JOINT_1].angle = angle
        elif selection == "2":
            angle = int(input("Joint 2 angle: "))
            angle = interp(angle, [-90, 90], [0, 180])  # add 90
            servo_kit.servo[PIN_JOINT_2].angle = angle
        elif selection == "3":
            angle = int(input("Joint 3 angle: "))
            angle = interp(angle, [-90, 90], [0, 180])  # add 90
            servo_kit.servo[PIN_JOINT_3].angle = angle
        elif selection == "G" or selection == "g":
            inches = float(input("Gripper distance (inches 0.0 to 2.0): "))
            angle = interp(inches, [0, 2], [100, 20])
            print("Request:", inches, " Result: ", angle)
            servo_kit.servo[PIN_GRIPPER_SERVO].angle = angle
        else:
            print("Invalid servo number")


main()
