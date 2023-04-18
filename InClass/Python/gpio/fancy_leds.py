import gpiozero as gz
import time
import signal

def main():
    print("Fancy LEDs")
    # fancy_blink()
    led_pwm()


def fancy_blink():
    print("Fancy blink")
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)

    # red_led.blink(4, 1, 3, False)
    # red_led.blink(off_time=0.2, background=False)
    red_led.blink()
    time.sleep(0.1)
    yellow_led.blink()
    time.sleep(0.1)
    green_led.blink()

    # time.sleep(5.0)
    signal.pause()

    print("Goodbye")


def led_pwm():
    print("Fancy blink")
    red_led = gz.PWMLED(14)
    yellow_led = gz.PWMLED(15)
    green_led = gz.PWMLED(18)

    while True:
        for k in range(100):
            red_led.value = k / 200
            time.sleep(0.01)

main()
