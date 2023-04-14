import gpiozero as gz
import time
import signal

def handle_color_press(leds, color, data):
    data += [color]
    # print("Pressed", color)
    print(data)
    show_led(leds, color)


def show_led(leds, color):
    if color == "R":
        leds.value = (1, 0 , 0)
    if color == "Y":
        leds.value = (0, 1 , 0)
    if color == "G":
        leds.value = (0, 0 , 1)
        
def run_sequence(leds, data):
    for color in data:
        show_led(leds, color)
        time.sleep(1)
        leds.off()
        time.sleep(0.1)
    
    data.clear()

def main():
    print("Ready")
    data = []
    leds = gz.LEDBoard(14, 15, 18)

    button_red = gz.Button(22)
    button_yellow = gz.Button(23)
    button_green = gz.Button(24)

    button_run = gz.Button(25)

    button_red.when_pressed = lambda : handle_color_press(leds, "R", data)
    button_yellow.when_pressed = lambda : handle_color_press(leds, "Y", data)
    button_green.when_pressed = lambda : handle_color_press(leds, "G", data)

    button_red.when_released = leds.off
    button_yellow.when_released = leds.off
    button_green.when_released = leds.off

    button_run.when_pressed = lambda : run_sequence(leds, data)

    signal.pause()


main()