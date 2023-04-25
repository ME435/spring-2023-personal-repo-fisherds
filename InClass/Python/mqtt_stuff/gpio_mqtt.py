import mqtt_helper as mh
import gpiozero as gz
import time

class App:
    def __init__(self):
        self.red_led = gz.LED(14)
        self.yellow_led = gz.LED(15)
        self.green_led = gz.LED(18)

        self.button25 = gz.Button(25)
        self.button25.when_pressed = lambda : self.mqtt_client.send_message("button")

        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.callback = lambda type, payload: self.my_callback(type, payload)
        self.mqtt_client.connect("me435/fisherds/to_pi", "me435/fisherds/to_computer2", use_off_campus_broker=True)


    def my_callback(self, message_type, message_payload):
        print(f"Type: {message_type}   Payload: {message_payload}")

        if message_type == "red":
            if message_payload == "on":
                self.red_led.on()
            if message_payload == "off":
                self.red_led.off()

        if message_type == "yellow":
            if message_payload == "on":
                self.yellow_led.on()
            if message_payload == "off":
                self.yellow_led.off()

        if message_type == "green":
            if message_payload == "on":
                self.green_led.on()
            if message_payload == "off":
                self.green_led.off()

def main():
    print("Ready")
    app = App()
    
    while True:
        # app.mqtt_client.send_message("button")  # Hacky test until we use a real button!
        time.sleep(0.1)
  

main()
