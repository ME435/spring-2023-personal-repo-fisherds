import gpiozero as gz
import time 
import signal

def main():
    print("Line Following")

    ultrasonic_sensor = gz.DistanceSensor(echo=8, trigger=11)
    left_line = gz.LineSensor(20)
    middle_line = gz.LineSensor(16)
    right_line = gz.LineSensor(19)

    right_motor_backwards_pin = gz.DigitalOutputDevice(14)
    right_motor_forwards_pin = gz.DigitalOutputDevice(15)
    right_motor_pwm_enable = gz.PWMOutputDevice(4)

    left_motor_forwards_pin = gz.DigitalOutputDevice(27)
    left_motor_backwards_pin = gz.DigitalOutputDevice(18)
    left_motor_pwm_enable = gz.PWMOutputDevice(17)

    left_motor_backwards_pin.off()
    right_motor_backwards_pin.off()
    left_motor_pwm_enable.value = 1.0
    right_motor_pwm_enable.value = 1.0
    
    left_line.when_line = lambda: left_motor_forwards_pin.on()
    left_line.when_no_line = lambda: left_motor_forwards_pin.off()
    right_line.when_line = lambda: right_motor_forwards_pin.on()
    right_line.when_no_line = lambda: right_motor_forwards_pin.off()

    signal.pause()


main()
