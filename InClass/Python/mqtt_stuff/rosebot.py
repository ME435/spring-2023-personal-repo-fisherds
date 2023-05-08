import adafruit_servokit
import numpy

class RoseBot:

    def __init__(self):
        self.arm_servos = ArmServos()
        # self.drive_system = 
        # self.ultrasonic = 
        # self.line_sensors = 


CHANNEL_JOINT_1 = 12
CHANNEL_JOINT_2 = 13
CHANNEL_JOINT_3 = 14
CHANNEL_GRIPPER = 15

class ArmServos:

    def __init__(self):
        self.servo_kit = adafruit_servokit.ServoKit(channels=16)

    def move_joints(self, angles):
        print(f"Moving the joints to {angles}")
        joint1_angle = numpy.interp(angles[0], [-90, 90], [180, 0])
        joint2_angle = numpy.interp(angles[1], [-90, 45], [0, 135])  
        joint3_angle = numpy.interp(angles[2], [-90, 90], [0, 180]) 
        self.servo_kit.servo[CHANNEL_JOINT_1].angle = joint1_angle
        self.servo_kit.servo[CHANNEL_JOINT_2].angle = joint2_angle
        self.servo_kit.servo[CHANNEL_JOINT_3].angle = joint3_angle

    def move_gripper(self, distance_in):
        print(f"Moving the gripper to {distance_in}")
        angle = numpy.interp(distance_in, [0, 2], [100, 10])  
        self.servo_kit.servo[CHANNEL_GRIPPER].angle = angle

    def disable(self):
        print(f"Turn all the arm servos off.")
        self.servo_kit.servo[CHANNEL_JOINT_1].angle = None
        self.servo_kit.servo[CHANNEL_JOINT_2].angle = None
        self.servo_kit.servo[CHANNEL_JOINT_3].angle = None
        self.servo_kit.servo[CHANNEL_GRIPPER].angle = None