import mqtt_helper as mh
import time

def my_callback(message_type, message_payload):
    print(f"Type: {message_type}   Payload: {message_payload}")

def main():
    print("Ready")
    mqtt_client = mh.MqttClient() # note, use "mqtt_helper.MqttClient" in other files
    mqtt_client.callback = lambda type, payload: my_callback(type, payload)
    mqtt_client.connect("my_messages", "my_messages", use_off_campus_broker=True)

    counter = 0
    while True:
        mqtt_client.send_message("chat", f"fisher {counter}")
        counter += 1
        time.sleep(2)
  

main()
