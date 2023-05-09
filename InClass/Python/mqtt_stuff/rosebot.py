import adafruit_servokit
import gpiozero as gz
import numpy

class RoseBot:

    def __init__(self):
        self.arm_servos = ArmServos()
        self.drive_system = DriveSystem()
        # self.ultrasonic = 
        self.line_sensors = LineSensors()


class LineSensors:

    def __init__(self):
        self.port_sensor = gz.LineSensor(19)
        self.center_sensor = gz.LineSensor(16)
        self.starboard_sensor = gz.LineSensor(20)

    def get_values(self):
        # Black is a value of 1
        # White is a value of 0
        return [self.port_sensor.value, self.center_sensor.value, self.starboard_sensor.value]


class DriveSystem:

    def __init__(self):
        self.left_motor = gz.Motor(forward=27, backward=18, enable=17)
        self.right_motor = gz.Motor(forward=15, backward=14, enable=4)

    def drive(self, message_payload):
        left_dir = message_payload[0]  # -1 is backwards, 0 is stop, 1 is forwards
        left_pwm = message_payload[1]
        right_dir = message_payload[2]
        right_pwm = message_payload[3]
        if left_dir == -1:
            self.left_motor.backward(left_pwm)
        elif left_dir == 0:
            self.left_motor.stop()
        elif left_dir == 1:
            self.left_motor.forward(left_pwm)
        else:
            print("Unknown direction given for left!")

        if right_dir == -1:
            self.right_motor.backward(right_pwm)
        elif right_dir == 0:
            self.right_motor.stop()
        elif right_dir == 1:
            self.right_motor.forward(right_pwm)
        else:
            print("Unknown direction given for right!")



class ArmServos:
    CHANNEL_JOINT_1 = 12
    CHANNEL_JOINT_2 = 13
    CHANNEL_JOINT_3 = 14
    CHANNEL_GRIPPER = 15

    def __init__(self):
        self.servo_kit = adafruit_servokit.ServoKit(channels=16)

    def move_joints(self, angles):
        print(f"Moving the joints to {angles}")
        joint1_angle = numpy.interp(angles[0], [-90, 90], [180, 0])
        joint2_angle = numpy.interp(angles[1], [-90, 45], [0, 135])  
        joint3_angle = numpy.interp(angles[2], [-90, 90], [0, 180]) 
        self.servo_kit.servo[ArmServos.CHANNEL_JOINT_1].angle = joint1_angle
        self.servo_kit.servo[ArmServos.CHANNEL_JOINT_2].angle = joint2_angle
        self.servo_kit.servo[ArmServos.CHANNEL_JOINT_3].angle = joint3_angle

    def move_gripper(self, distance_in):
        print(f"Moving the gripper to {distance_in}")
        angle = numpy.interp(distance_in, [0, 2], [100, 10])  
        self.servo_kit.servo[ArmServos.CHANNEL_GRIPPER].angle = angle

    def disable(self):
        print(f"Turn all the arm servos off.")
        self.servo_kit.servo[ArmServos.CHANNEL_JOINT_1].angle = None
        self.servo_kit.servo[ArmServos.CHANNEL_JOINT_2].angle = None
        self.servo_kit.servo[ArmServos.CHANNEL_JOINT_3].angle = None
        self.servo_kit.servo[ArmServos.CHANNEL_GRIPPER].angle = None