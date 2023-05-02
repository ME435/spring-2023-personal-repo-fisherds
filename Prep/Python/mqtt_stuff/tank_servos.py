import mqtt_helper
import adafruit_servokit
import numpy
import time

CHANNEL_JOINT_1 = 12
CHANNEL_JOINT_2 = 13
CHANNEL_JOINT_3 = 14
CHANNEL_GRIPPER = 15

class App:
    def __init__(self):
        self.servo_kit = adafruit_servokit.ServoKit(channels=16)

        self.mqtt_client = mqtt_helper.MqttClient()
        self.mqtt_client.callback = self.mqtt_callback
        self.mqtt_client.connect(
            use_off_campus_broker=True,
            subscription_topic_name="me435/fisherds/to_pi",
            publish_topic_name="me435/fisherds/to_computer")

    def mqtt_callback(self, message_type, payload):
        print("MQTT message_type", message_type)
        print("MQTT payload", payload)

        if message_type == "joints":
            joint1_angle = numpy.interp(payload[0], [-90, 90], [180, 0])  # flip
            joint2_angle = numpy.interp(payload[1], [-90, 90], [0, 180])  # add 90
            joint3_angle = numpy.interp(payload[2], [-90, 90], [0, 180])  # add 90
            self.servo_kit.servo[CHANNEL_JOINT_1].angle = joint1_angle
            self.servo_kit.servo[CHANNEL_JOINT_2].angle = joint2_angle
            self.servo_kit.servo[CHANNEL_JOINT_3].angle = joint3_angle

        if message_type == "gripper":
            servo_angle = numpy.interp(payload, [0, 2], [105, 0])
            self.servo_kit.servo[CHANNEL_GRIPPER].angle = servo_angle


def main():
    print("MQTT Servos")
    app = App()
    while True:
        time.sleep(0.01)


main()
