import adafruit_servokit
from numpy import interp
import gpiozero as gz
import time

class RoseBot:
  def __init__(self):
    self.drive_system = DriveSystem()
    self.arm_servos = ArmServos()
    self.ultrasonic = UltrasonicSensor()
    self.line_sensors = LineSensors()

class Motor:
  def __init__(self, pin_1, pin_2, pin_enable):
    self.digital_output_1 = gz.DigitalOutputDevice(pin_1)
    self.digital_output_2 = gz.DigitalOutputDevice(pin_2)
    self.pwm_output = gz.PWMOutputDevice(pin_enable,frequency=1000)

  def turn_on(self, duty_cycle):
    if duty_cycle > 0:
      self.digital_output_1.on()
      self.digital_output_2.off()
      self.pwm_output.value = duty_cycle / 100.0
    elif duty_cycle < 0:
      self.digital_output_1.off()
      self.digital_output_2.on()
      self.pwm_output.value = -duty_cycle / 100.0
    else:
      self.turn_off()

  def turn_off(self):
    self.digital_output_1.off()
    self.digital_output_2.off()
    self.pwm_output.value = 0


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


class ArmServos:
  PIN_JOINT_1 = 12
  PIN_JOINT_2 = 13
  PIN_JOINT_3 = 14
  PIN_GRIPPER_SERVO = 15

  def __init__(self):
    self.kit = adafruit_servokit.ServoKit(channels=16)
  
  def set_joint_angle(self, joint_number, angle):
    pin = joint_number + ArmServos.PIN_CAMERA_SERVO  # 12, 13, or 14
    if joint_number == 1:
      servo_angle = interp(angle, [-90, 90], [180, 0])  # flip
    else:
      servo_angle = interp(angle, [-90, 90], [0, 180])  # add 90
    self.kit.servo[pin].angle = servo_angle
  
  def set_gripper_inches(self, inches):
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
    def __init__(self):
        self.left_line = gz.LineSensor(20)
        self.middle_line = gz.LineSensor(16)
        self.right_line = gz.LineSensor(19)

    def get_left_value(self):
        return self.left_line.value

    def get_middle_value(self):
        return self.middle_line.value

    def get_right_value(self):
        return self.right_line.value

