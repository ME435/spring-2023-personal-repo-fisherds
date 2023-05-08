import mqtt_helper as mh
import time
import rosebot

class App:
    def __init__(self):
        self.robot = rosebot.RoseBot()

        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.callback = self.my_callback
        self.mqtt_client.connect(subscription_topic_name="me435/fisherds/to_pi",
                                 publish_topic_name="me435/fisherds/to_computer",
                                 use_off_campus_broker=True)


    def my_callback(self, message_type, message_payload):
        print(f"Type: {message_type}   Payload: {message_payload}")

        if message_type == "joints":
            print(f"Moving the joints to {message_payload}")
            self.robot.arm_servos.move_joints(message_payload)
            
        if message_type == "gripper":
            print(f"Moving the gripper to {message_payload}")
            self.robot.arm_servos.move_gripper(message_payload)
            
        if message_type == "arm_off":
            print(f"Turn all the arm servos off.")
            self.robot.arm_servos.disable()
            
        if message_type == "drive":
            print(f"Drive the tank treads at {message_payload}.")
            # TODO: use the rosebot class


def main():
    print("Ready")
    app = App()
    
    while True:
        time.sleep(0.1)
  

main()
