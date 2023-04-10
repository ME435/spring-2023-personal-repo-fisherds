import gpiozero as gz
import time

def main():
    print("Ready")
    # sweep()
    menu()

def menu():
    servo = gz.AngularServo(17)

    while True:
        # servo.angle = -90
        # time.sleep(2)
        # servo.angle = 90
        # time.sleep(2)
        angle_str = input("Angle: ")
        if angle_str == "":
            print("Goodbye")
            break
        servo.angle = int(angle_str)
    

def sweep():
    servo = gz.Servo(17)
    while True:
        servo.min()
        time.sleep(2)
        servo.mid()
        time.sleep(2)
        servo.max()
        time.sleep(2)   

main()
