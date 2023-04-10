import gpiozero as gz
import time

def main():
    print("Ready")
    # basic_led_on_off()
    # manual_blink()
    manual_traffic_light()


def basic_led_on_off():
    print("All On")
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)

    red_led.on()
    yellow_led.on()
    green_led.on()

    time.sleep(3)
    print("All Off")


def manual_blink():
    print("Manual Blink")
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)

    for k in range(5):
        red_led.on()
        yellow_led.on()
        green_led.on()

        time.sleep(1)

        red_led.off()
        yellow_led.off()
        green_led.off()

        time.sleep(1)


def manual_traffic_light():
    print("Manual Traffic Light")
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)

    while True:
        red_led.on()
        time.sleep(5)
        red_led.off()

        green_led.on()
        time.sleep(3)
        green_led.off()

        yellow_led.on()
        time.sleep(1)
        yellow_led.off()

main()
