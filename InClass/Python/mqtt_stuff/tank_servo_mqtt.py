import mqtt_helper as mh
import time
import adafruit_servokit
import numpy

CHANNEL_JOINT_1 = 12
CHANNEL_JOINT_2 = 13
CHANNEL_JOINT_3 = 14
CHANNEL_GRIPPER = 15


class App:
    def __init__(self):
        self.servo_kit = adafruit_servokit.ServoKit(channels=16)

        self.mqtt_client = mh.MqttClient()
        # self.mqtt_client.callback = lambda type, payload: self.my_callback(type, payload)
        self.mqtt_client.callback = self.my_callback
        self.mqtt_client.connect(subscription_topic_name="me435/fisherds/to_pi",
                                 publish_topic_name="me435/fisherds/to_computer",
                                 use_off_campus_broker=True)


    def my_callback(self, message_type, message_payload):
        # print(f"Type: {message_type}   Payload: {message_payload}")

        if message_type == "joints":
            # print(f"Moving the joints to {message_payload}")
            joint1_angle = numpy.interp(message_payload[0], [-90, 90], [180, 0])
            joint2_angle = numpy.interp(message_payload[1], [-90, 45], [0, 135])  
            joint3_angle = numpy.interp(message_payload[2], [-90, 90], [0, 180]) 
            self.servo_kit.servo[CHANNEL_JOINT_1].angle = joint1_angle
            self.servo_kit.servo[CHANNEL_JOINT_2].angle = joint2_angle
            self.servo_kit.servo[CHANNEL_JOINT_3].angle = joint3_angle

        if message_type == "gripper":
            # print(f"Moving the gripper to {message_payload}")
            angle = numpy.interp(message_payload, [0, 2], [100, 10])  
            self.servo_kit.servo[CHANNEL_GRIPPER].angle = angle


def main():
    print("Ready")
    app = App()
    
    while True:
        time.sleep(0.1)
  

main()
