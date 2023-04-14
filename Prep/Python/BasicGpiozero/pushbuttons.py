import gpiozero as gz
import time
import signal

def main():
    print("Ready")
    # read_button_state()
    button_interrupts()

def read_button_state():
    button = gz.Button(25)

    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)

    while True:
        if button.is_pressed:
            red_led.on()
            # print("Button is pressed")
            
        else:
            red_led.off()
            # print("Button is not pressed")
        time.sleep(0.1)

def say_hello():
    print("Hello")


def say_message(msg):
    print(f"Message: {msg}")


def button_interrupts():
    button = gz.Button(25)
    # button.when_pressed = say_hello
    # button.when_pressed = lambda : say_hello()

    button.when_pressed = lambda : say_message("Press")
    button.when_released = lambda : say_message("Release")

    signal.pause()


main()
