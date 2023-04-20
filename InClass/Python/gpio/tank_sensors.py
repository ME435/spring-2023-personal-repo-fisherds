import gpiozero as gz
import time
import signal


def main():
    print("Tank Sensors")
    # line_sensor_events()
    # line_sensor_states()
    ultrasonic_distance_sensor()

def ultrasonic_distance_sensor():
    print("Ultrasonic Distance Sensor")

    
def line_sensor_states():
    print("Line Sensor States")
    starboard_line_sensor = gz.LineSensor(20)
    port_line_sensor = gz.LineSensor(19)
    middle_line_sensor = gz.LineSensor(16)
    
    while True:
        print(f"Starboard: {starboard_line_sensor.value} Middle: {middle_line_sensor.value}  Port: {port_line_sensor.value}")
        # Black is a value of 1
        # White is a value of 0
        time.sleep(1.0)

def line_sensor_events():
    print("Line Sensor Events")
    starboard_line_sensor = gz.LineSensor(20)
    port_line_sensor = gz.LineSensor(19)
    middle_line_sensor = gz.LineSensor(16)

    starboard_line_sensor.when_line = lambda: print("Starboard: white!")
    starboard_line_sensor.when_no_line = lambda: print("Starboard: black!")
    
    middle_line_sensor.when_line = lambda: print("Middle: white!")
    middle_line_sensor.when_no_line = lambda: print("Middle: black!")
    
    port_line_sensor.when_line = lambda: print("Port: white!")
    port_line_sensor.when_no_line = lambda: print("Port: black!")
    
    signal.pause()

main()
