import gpiozero as gz
import time 
import signal

def main():
    print("Sensor test")

    ultrasonic_sensor = gz.DistanceSensor(echo=8, trigger=11)
    left_line = gz.LineSensor(20)
    middle_line = gz.LineSensor(16)
    right_line = gz.LineSensor(19)

    # while True:
    #     print("      {:5.1f}                         {}      {}      {}".format(
    #         ultrasonic_sensor.distance * 100,
    #         "W" if left_line.value == 0 else "B",
    #         "W" if middle_line.value == 0 else "B",
    #         "W" if right_line.value == 0 else "B"))
    #     time.sleep(1)

    left_line.when_line = lambda: print('Line detected')
    left_line.when_no_line = lambda: print('No line detected')
    signal.pause()



main()
