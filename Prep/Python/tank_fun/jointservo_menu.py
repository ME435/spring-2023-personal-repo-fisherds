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

    PIN_CAMERA_SERVO = 11
    PIN_JOINT_1 = 12
    PIN_JOINT_2 = 13
    PIN_JOINT_3 = 14
    PIN_GRIPPER_SERVO = 15

    servo_kit = adafruit_servokit.ServoKit(channels=16)

    while True:

        print("Type in a servo number.  Options:")
        print("11 --> Camera Tilt")
        print("12 --> Arm Joint 1")
        print("13 --> Arm Joint 2")
        print("14 --> Arm Joint 3")
        print("15 --> Gripper")
        servo_number = int(input("Servo number (11 to 15) or (0 to exit): "))
        if servo_number == 0:
            break
        elif servo_number == 11:
            angle = int(input("Camera title angle (0 to 60): "))
            servo_angle = interp(angle,[0, 45], [30, 0]) # maps 0->45 to 30->0 (flip and scale)
            servo_kit.servo[PIN_CAMERA_SERVO].angle = servo_angle
        elif servo_number == PIN_JOINT_1:
            angle = int(input("Joint 1 angle (-90 to 90): "))
            servo_angle = interp(angle, [-90, 90], [180, 0])  # flip
            servo_kit.servo[PIN_JOINT_1].angle = servo_angle
        elif servo_number == PIN_JOINT_2:
            angle = int(input("Joint 2 angle (-90 to 90): "))
            servo_angle = interp(angle, [-90, 90], [0, 180])  # add 90
            servo_kit.servo[PIN_JOINT_2].angle = servo_angle
        elif servo_number == PIN_JOINT_3:
            angle = int(input("Joint 3 angle (-90 to 90): "))
            servo_angle = interp(angle, [-90, 90], [0, 180])  # add 90
            servo_kit.servo[PIN_JOINT_3].angle = servo_angle
        elif servo_number == 15:
            distance_inches = float(input("Gripper distance (inches 0.0 to 2.0): "))
            servo_angle = interp(inches, [0, 2], [105, 0])
            print("Request:", inches, " Result: ", servo_angle)
            servo_kit.servo[PIN_GRIPPER_SERVO].angle = servo_angle
        else:
            print("Invalid servo number")


main()
