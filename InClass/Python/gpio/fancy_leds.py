import gpiozero as gz
import time
import signal

def main():
    print("Fancy LEDs")
    # fancy_blink()
    # led_pwm()
    # led_board()
    traffic_light_api()


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
    print("LED PWM")
    red_led = gz.PWMLED(14)
    yellow_led = gz.PWMLED(15)
    green_led = gz.PWMLED(18)

    while True:
        for k in range(100):
            red_led.value = k / 200
            time.sleep(0.01)



def led_board():
    print("LED Board")
    leds = gz.LEDBoard(14, 15, 18, pwm=True)

    leds.on()
    time.sleep(1)
    
    leds.off()
    time.sleep(1)
    
    leds.value = (1, 0, 1)
    time.sleep(1)
    
    leds.value = (0.2, 0.2, 0.2)
    time.sleep(1)
    
    leds.blink()
    signal.pause()


def traffic_light_api():
    print("TrafficLight api")
    # Create a TrafficLights object

    # Loop forever
    #   Green LED on only for 4 seconds (using TrafficLights object)
    #   Yellow LED on only for 1 seconds
    #   Red LED on only for 3 seconds


main()
