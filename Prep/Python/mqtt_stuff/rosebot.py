import adafruit_servokit
from numpy import interp
import gpiozero as gz
import time


class RoseBot:
  def __init__(self):
    self.mode = ""
    self.drive_system = DriveSystem()
    self.arm_servos = ArmServos()
    self.ultrasonic = UltrasonicSensor()
    self.line_sensors = LineSensors()
  
  def set_mode(self, mode):
    self.mode = mode
    if self.mode == "go_until_wall" or "go_until_line":
      self.drive_system.go_forward()    
    if self.mode == "":
      self.drive_system.stop()
     
  def update_mode(self):
    if self.mode == "go_until_wall":
      if self.ultrasonic.get_distance() < 20.0:
        self.drive_system.stop()
        self.mode = ""
    
    if self.mode == "go_until_line":
      for reading in self.line_sensors.get_values():
        if reading == LineSensors.BLACK:
          self.drive_system.stop()
          self.mode = ""
    
    if self.mode == "line_follow":
      self.do_line_follow()    
    
  def do_line_follow(self):
    line_sensor_readings = self.line_sensors.get_values()
    # Algorithm from Evan Cruise
    if line_sensor_readings == [0, 1, 0]:
        # in middle: both motors forward
        print("Go forwards")
        self.drive_system.go_forward(0.5)
    elif line_sensor_readings == [1, 1, 0]:
        # turn slightly left: left motor reverse slow, keep right motor on at high speed
        print("Slight left turn")
        self.drive_system.turn_left(0.25, 0.5)
    elif line_sensor_readings == [1, 0, 0]:
        # turn hard left: left motor reverse high, keep right motor on at high speed
        print("Sharp left turn")
        self.drive_system.turn_left(0.5, 0.5)
    elif line_sensor_readings == [0, 1, 1]:
        # turn slightly right: right motor reverse slow, keep left motor on at high speed
        print("Slight right turn")
        self.drive_system.turn_right(0.5, 0.25)
    elif line_sensor_readings == [0, 0, 1]:
        # turn hard right: right motor reverse high, keep left motor on at high speed
        print("Sharp right turn")
        self.drive_system.turn_right(0.5, 0.5)


class DriveSystem:
  def __init__(self):
    Motor_A_EN = 4
    Motor_B_EN = 17
    Motor_A_Pin1 = 14
    Motor_A_Pin2 = 15
    Motor_B_Pin1 = 27
    Motor_B_Pin2 = 18
    self.left_motor = gz.Motor(forward=Motor_B_Pin1, backward=Motor_B_Pin2, enable=Motor_B_EN)
    self.right_motor =gz.Motor(forward=Motor_A_Pin2, backward=Motor_A_Pin1, enable=Motor_A_EN)

  def stop(self):
     self.left_motor.stop()
     self.right_motor.stop()

  def drive(self, message_payload):
     self.drive_motor(self.left_motor, message_payload[0], message_payload[1])
     self.drive_motor(self.right_motor, message_payload[2], message_payload[3])

  def go_forward(self, pwm=0.6):
     self.left_motor.forward(pwm)
     self.right_motor.forward(pwm)
  
  def go_backward(self, pwm=0.6):
     self.left_motor.reverse(pwm)
     self.right_motor.reverse(pwm)
  
  def turn_right(self, leftMotorSpeed, rightMotorSpeed):
     self.left_motor.forward(leftMotorSpeed)
     self.right_motor.reverse(rightMotorSpeed)

  def turn_left(self, leftMotorSpeed, rightMotorSpeed):
     self.left_motor.reverse(leftMotorSpeed)
     self.right_motor.forward(rightMotorSpeed)
  
  def drive_motor(self, motor: gz.Motor, direction, pwm):
    if direction == 0:
      motor.stop()
    elif direction == 1:
       motor.forward(pwm)
    elif direction == -1:
       motor.reverse(pwm)
        

class ArmServos:
  PIN_JOINT_1 = 12
  PIN_JOINT_2 = 13
  PIN_JOINT_3 = 14
  PIN_GRIPPER_SERVO = 15

  def __init__(self):
    self.kit = adafruit_servokit.ServoKit(channels=16)
  
  def move_joints(self, angles):
     self.move_joints(1, angles[0])
     self.move_joints(2, angles[1])
     self.move_joints(3, angles[2])
     
  def set_joint_angle(self, joint_number, angle):
    pin = joint_number + 11  # Little hack to get --> 12, 13, or 14
    if joint_number == 1:
      servo_angle = interp(angle, [-90, 90], [180, 0])  # flip
    else:
      servo_angle = interp(angle, [-90, 90], [0, 180])  # add 90
    self.kit.servo[pin].angle = servo_angle
  
  def move_gripper(self, inches):
    servo_angle = interp(inches, [0, 2], [105, 0])
    print("Request:", inches, " Result: ", servo_angle)
    self.kit.servo[ArmServos.PIN_GRIPPER_SERVO].angle = servo_angle

  def disable(self):
    self.kit.servo[ArmServos.PIN_JOINT_1].angle = None
    self.kit.servo[ArmServos.PIN_JOINT_2].angle = None
    self.kit.servo[ArmServos.PIN_JOINT_3].angle = None
    self.kit.servo[ArmServos.PIN_GRIPPER_SERVO].angle = None


class UltrasonicSensor:
    def __init__(self):
        self.sensor = gz.DistanceSensor(echo=8, trigger=11)

    # return distance in cm
    def get_distance(self):
        return self.sensor.distance * 100


class LineSensors:
    BLACK = 0
    WHITE = 1

    def __init__(self):
        self.left_line = gz.LineSensor(20)
        self.middle_line = gz.LineSensor(16)
        self.right_line = gz.LineSensor(19)

    def get_values(self):
       return [self.left_line.value, self.middle_line.value, self.right_line.value]

    def get_left_value(self):
        return self.left_line.value  # I think maybe 1 is white???

    def get_middle_value(self):
        return self.middle_line.value

    def get_right_value(self):
        return self.right_line.value

