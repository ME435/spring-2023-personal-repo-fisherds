import mqtt_helper as mh
import gpiozero as gz
import time

class App:
    def __init__(self):
        self.red_led = gz.LED(14)
        self.yellow_led = gz.LED(15)
        self.green_led = gz.LED(18)

        self.button22 = gz.Button(22)
        self.button22.when_pressed = lambda : self.mqtt_client.send_message("button", 1)

        self.button23 = gz.Button(23)
        self.button23.when_pressed = lambda : self.mqtt_client.send_message("button", 10)

        self.button24 = gz.Button(24)
        self.button24.when_pressed = lambda : self.mqtt_client.send_message("button", 100)

        self.button25 = gz.Button(25)
        self.button25.when_pressed = lambda : self.mqtt_client.send_message("reset")

        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.callback = lambda type, payload: self.my_callback(type, payload)
        self.mqtt_client.connect("me435/fisherds/to_pi", "me435/fisherds/to_computer", use_off_campus_broker=True)


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

        if message_type == "leds":
            print("TODO: Process the leds payload:")
            print(message_payload)

def main():
    print("Ready")
    app = App()
    
    while True:
        # app.mqtt_client.send_message("button")  # Hacky test until we use a real button!
        time.sleep(0.1)
  

main()
