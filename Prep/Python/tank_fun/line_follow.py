import gpiozero as gz
import time 
import signal

def main():
    print("Line Following")

    ultrasonic_sensor = gz.DistanceSensor(echo=8, trigger=11)
    left_line = gz.LineSensor(19)
    middle_line = gz.LineSensor(16)
    right_line = gz.LineSensor(20)

    right_motor_backwards_pin = gz.DigitalOutputDevice(14)
    right_motor_forwards_pin = gz.DigitalOutputDevice(15)
    right_motor_pwm_enable = gz.PWMOutputDevice(4)

    left_motor_forwards_pin = gz.DigitalOutputDevice(27)
    left_motor_backwards_pin = gz.DigitalOutputDevice(18)
    left_motor_pwm_enable = gz.PWMOutputDevice(17)

    left_motor_forwards_pin.on()
    left_motor_backwards_pin.off()
    left_motor_pwm_enable.value = 0.6

    right_motor_forwards_pin.on()
    right_motor_backwards_pin.off()
    right_motor_pwm_enable.value = 0.8

    while True:
        if left_line.value == 0:
            left_motor_forwards_pin.on()
        else:
            left_motor_forwards_pin.off()

        if right_line.value == 0:
            right_motor_forwards_pin.on()
        else:
            right_motor_forwards_pin.off()


main()
