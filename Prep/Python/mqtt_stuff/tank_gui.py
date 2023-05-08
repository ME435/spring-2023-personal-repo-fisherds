import mqtt_helper as mh
import gpiozero as gz
import rosebot
import time

class App:

    def __init__(self):
        self.robot = rosebot.RoseBot()

        self.mqtt_client = mh.MqttClient() # note, use "mqtt_helper.MqttClient" in other files
        self.mqtt_client.callback = lambda type, payload: self.my_callback(type, payload)
        # self.mqtt_client.connect("fisherds/#", "fisherds/to_computer", use_off_campus_broker=True)
        self.mqtt_client.connect("fisherds/to_pi", "fisherds/to_computer", use_off_campus_broker=True)

        self.button25.when_pressed = lambda : self.mqtt_client.send_message("button")



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
