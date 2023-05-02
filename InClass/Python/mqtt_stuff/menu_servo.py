import adafruit_servokit
import numpy

CHANNEL_JOINT_1 = 12
CHANNEL_JOINT_2 = 13
CHANNEL_JOINT_3 = 14
CHANNEL_GRIPPER = 15


def main():
    print("Servo Menu")

    servo_kit = adafruit_servokit.ServoKit(channels=16)


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
            angle = numpy.interp(angle, [-90, 90], [180, 0])
            servo_kit.servo[CHANNEL_JOINT_1].angle = angle
            
        elif selection == "2":
            angle = int(input("Joint 2 angle: "))
            # This angle should be 0 to 180, BE CAREFUL!!!!!!
            angle = numpy.interp(angle, [-90, 45], [0, 135])  
            servo_kit.servo[CHANNEL_JOINT_2].angle = angle
            
        elif selection == "3":
            angle = int(input("Joint 3 angle: "))
            # This angle should be 0 to 180, we'll start here!
            angle = numpy.interp(angle, [-90, 90], [0, 180])  
            servo_kit.servo[CHANNEL_JOINT_3].angle = angle
            
        elif selection == "G" or selection == "g":
            inches = float(input("Gripper distance: "))
            # tranlate inches into servo angle
            # This angle should be 0 to 180!
            angle = numpy.interp(inches, [0, 2], [100, 10])  
            servo_kit.servo[CHANNEL_GRIPPER].angle = angle
        
        else:
            print("Invalid selection")

main()
