import gpiozero as gz
import time

def main():
    print("Ready")
    # Make DigitalOutputDevices for the motor pins
    right_motor_backwards_pin = gz.DigitalOutputDevice(14)
    right_motor_forwards_pin = gz.DigitalOutputDevice(15)
    right_motor_pwm_enable = gz.PWMOutputDevice(4)

    left_motor_forwards_pin = gz.DigitalOutputDevice(27)
    left_motor_backwards_pin = gz.DigitalOutputDevice(18)
    left_motor_pwm_enable = gz.PWMOutputDevice(17)

    # Make 1 motor go forward to 3 seconds
    # right_motor_forwards_pin.off()
    # right_motor_backwards_pin.off()
    # right_motor_pwm_enable.value = 0.0

    # left_motor_forwards_pin.on()
    # left_motor_backwards_pin.off()
    # left_motor_pwm_enable.value = 1.0

    # time.sleep(3.0)

    # left_motor_forwards_pin.off()
    # left_motor_backwards_pin.off()
    # left_motor_pwm_enable.value = 0.0
    # time.sleep(1.0)

    # Make the other motor go forward to 3 seconds
    # right_motor_forwards_pin.on()
    # right_motor_backwards_pin.off()
    # right_motor_pwm_enable.value = 1.0

    # left_motor_forwards_pin.off()
    # left_motor_backwards_pin.off()
    # left_motor_pwm_enable.value = 0.0

    # time.sleep(3.0)

    # right_motor_forwards_pin.off()
    # right_motor_backwards_pin.off()
    # right_motor_pwm_enable.value = 0.0
    # time.sleep(1.0)

    # Make both motors go forward to 3 seconds
    right_motor_forwards_pin.on()
    right_motor_backwards_pin.off()
    right_motor_pwm_enable.value = 1.0

    left_motor_forwards_pin.on()
    left_motor_backwards_pin.off()
    left_motor_pwm_enable.value = 1.0

    time.sleep(3.0)

    right_motor_forwards_pin.off()
    right_motor_backwards_pin.off()
    right_motor_pwm_enable.value = 0.0

    left_motor_forwards_pin.off()
    left_motor_backwards_pin.off()
    left_motor_pwm_enable.value = 0.0


main()
