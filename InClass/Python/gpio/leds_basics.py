import gpiozero as gz
import time

def main():
    print("Ready")
    # basic_on_off()
    traffic_light()


def basic_on_off():
    print("Basic on off control")
    red_led = gz.DigitalOutputDevice(14)
    yellow_led = gz.DigitalOutputDevice(15)
    green_led = gz.DigitalOutputDevice(18)

    for _ in range(5):
        red_led.on()
        yellow_led.on()
        green_led.on()

        time.sleep(1.0)

        red_led.off()
        yellow_led.off()
        green_led.off()

        time.sleep(1.0)


def traffic_light():
    print("Manual traffic light")
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)

    # Loop forever
    #   Green LED on only for 4 seconds
    #   Yellow LED on only for 1 seconds
    #   Red LED on only for 3 seconds


main()
