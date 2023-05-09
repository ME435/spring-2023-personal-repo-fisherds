import mqtt_helper as mh
import rosebot
import time
import datetime


class App:

    def __init__(self):
        self.robot = rosebot.RoseBot()

        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.callback = self.my_callback
        self.mqtt_client.connect("me435/fisherds/to_pi", "me435/fisherds/to_computer", use_off_campus_broker=True)

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
        
        if message_type == "line_sensor_stream":
            if message_payload.upper() == "On".upper():
                self.robot.is_streaming_line_sensors = True
            elif message_payload.upper() == "Off".upper():
                self.robot.is_streaming_line_sensors = False
            else:
                print("Unexpected line_sensor_stream payload")

        if message_type == "mode":
            print(f"Set mode to {message_payload}.")
            self.robot.set_mode(message_payload)


def main():
    print("Ready")
    app = App()

    last_sensor_send_time = time.time()
    while True:
        if app.robot.is_streaming_line_sensors and time.time() - last_sensor_send_time > 2:
            last_sensor_send_time = time.time()
            payload = {}
            payload["values"] = app.robot.line_sensors.get_values()
            now = datetime.datetime.now()
            payload["timestamp"] = now.strftime("%d/%m/%Y %H:%M:%S")
            print("payload =", payload)
            app.mqtt_client.send_message("line_sensors", payload)
        app.robot.update_mode()
        time.sleep(0.1)
  

main()
