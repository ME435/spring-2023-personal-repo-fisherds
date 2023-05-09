import mqtt_helper as mh
import time
import rosebot
import datetime

class App:
    def __init__(self):
        self.is_line_sensor_streaming = False
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
            self.robot.drive_system.drive(message_payload)

        if message_type == "line_streaming":
            if message_payload == "On":
                print("Turning on line streaming!")
                self.is_line_sensor_streaming = True
            elif message_payload == "Off":
                print("Turning off line streaming!")
                self.is_line_sensor_streaming = False
            else:
                print(f"Unknown streaming payload {message_payload}")


def main():
    print("Ready")
    app = App()
    
    last_message_time = time.time()
    while True:
        if app.is_line_sensor_streaming and time.time() - last_message_time > 2.0:
            last_message_time = time.time()
            # From: https://www.programiz.com/python-programming/datetime/strftime
            now = datetime.datetime.now() # current date and time
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            # print("date and time:", date_time)
            print(f"values: ", app.robot.line_sensors.get_values())
            app.mqtt_client.send_message("line_sensors", {"value": app.robot.line_sensors.get_values(),
                                                          "timestamp": date_time})

        time.sleep(0.1)
  

main()
