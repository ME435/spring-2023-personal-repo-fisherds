import gpiozero as gz
import time
import signal

def main():
    print("Pushbuttons")
    # Pushbutton on 25
    # also on 22, 23, 24 for the sequence repeater lab.
    # button_states()
    button_events()

def button_states():
    print("Button States")
    button25 = gz.Button(25)
    red_led = gz.LED(14)

    while True:
        # if button25.value == 1:
        # if button25.is_pressed:
        # if button25.is_active:
        if button25.is_held:   # Defaults to 1.0 seconds
            red_led.on()
        else:
            red_led.off()
        time.sleep(0.1)


def say_hello():
    print("Hello, you pressed the button")
    red_led = gz.LED(14)
    red_led.on()
    time.sleep(1.0)

def say_goodbye():
    print("Goodbye, you released the button")
    red_led = gz.LED(14)
    red_led.off()

def turn_leds_on(red_led, yellow_led, green_led):
    red_led.on()
    yellow_led.on()
    green_led.on()

def turn_leds_off(red_led, yellow_led, green_led):
    red_led.off()
    yellow_led.off()
    green_led.off()

def button_events():
    print("Button Events")
    button25 = gz.Button(25)
    # button25.when_pressed = say_hello
    # button25.when_released = say_goodbye

    # red_led = gz.LED(14)
    # button25.when_pressed = red_led.on
    # button25.when_released = red_led.off
    # print(type(say_hello))

    # silly_name = lambda arg1: print("Hello Class!", arg1)
    # button25.when_pressed = silly_name
    # button25.when_released = lambda : print("Goodbye Class!")

    # red_led = gz.LED(14)
    # button25.when_pressed = lambda : red_led.on()
    # button25.when_released = lambda : red_led.off()

    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)
    button25.when_pressed = lambda : turn_leds_on(red_led, yellow_led, green_led)
    button25.when_released = lambda : turn_leds_off(red_led, yellow_led, green_led)
    

    signal.pause()


main()
