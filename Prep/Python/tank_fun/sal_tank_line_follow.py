import gpiozero as gz
import time
import signal

def main():
    #line_sensor_states()
    #ultrasonic_distance_sensor()
    line_follow()

def ultrasonic_distance_sensor():
    print("Ultrasonic")
    sensor = gz.DistanceSensor(echo=8, trigger=11)
    while True:
        print('Distance: ', sensor.distance * 100)
        time.sleep(1)

def line_sensor_states():
    right_line_sensor = gz.LineSensor(20)
    left_line_sensor = gz.LineSensor(19)
    middle_line_sensor = gz.LineSensor(16)

    while True:
        print(f"Right: {right_line_sensor.value} Middle: {middle_line_sensor.value} Port: {left_line_sensor.value}")
        #Black 1
        #White 0
        time.sleep(1.0)

def right_no_line(left, right, left_f, left_b, right_b, right_f):
    print("Right no line")  
    left_f.off()
    left_b.on()
    right_f.on()
    right_b.off()
    right.value = .5
    left.value = .5

def right_line(left, right,left_f, left_b, right_b, right_f):
    print("Right line")
    left_f.on()
    left_b.off()
    right_f.on()
    right_b.off()
    right.value = .5
    left.value = .5
   
def left_no_line(left, right, left_f, left_b, right_b, right_f):
    print("Left no line")
    left_f.on()
    left_b.off()
    right_b.on()
    right_f.off()
    right.value = .5
    left.value = .5

def left_line(left, right, left_f, left_b, right_b, right_f):
    print("Left line")
    left_f.on()
    left_b.off()
    right_f.on()
    right_b.off()
    right.value = .5
    left.value = .5  

def drive_forward(left, right, left_f, left_b, right_b, right_f):
    left_f.on()
    left_b.off()
    right_f.on()
    right_b.off()
    right.value = .5
    left.value = .5  
    print("Middle")

def drive_stop(motor1, motor2):
    motor1.value = 0
    motor2.value = 0

def drive_correct(left, right, left_f, left_b, right_b, right_f, left_sensor, right_sensor):
    print("Middle no line")
    if left_sensor.line_detected: #line not detected
        left_no_line(left, right, left_f, left_b, right_b, right_f)
    elif right_sensor.line_detected:
        right_no_line(left, right, left_f, left_b, right_b, right_f)

def line_follow():
    data = [1, 1, 1]
    right_line_sensor = gz.LineSensor(20)
    left_line_sensor = gz.LineSensor(19)
    middle_line_sensor = gz.LineSensor(16)

    pin1A = gz.DigitalOutputDevice(14)
    pin1B = gz.DigitalOutputDevice(15)
    enable1 = gz.PWMOutputDevice(4)

    pin2A = gz.DigitalOutputDevice(27)
    pin2B = gz.DigitalOutputDevice(18)
    enable2 = gz.PWMOutputDevice(17)

    pin1A.on() #left forward
    pin1B.off() #left back
    pin2A.off() #right back
    pin2B.on()  #right forward

    right_line_sensor.when_line = lambda: right_no_line(enable1, enable2, pin1A, pin1B, pin2A, pin2B)      #no line
    right_line_sensor.when_no_line = lambda: right_line(enable1, enable2, pin1A, pin1B, pin2A, pin2B)      #line

    left_line_sensor.when_line = lambda: left_no_line(enable1, enable2, pin1A, pin1B, pin2A, pin2B)        #no line
    left_line_sensor.when_no_line = lambda: left_line(enable1, enable2, pin1A, pin1B, pin2A, pin2B)        #line

    middle_line_sensor.when_line = lambda:  drive_correct(enable1, enable2, pin1A, pin1B, pin2A, pin2B, left_line_sensor, right_line_sensor)    #no line
    middle_line_sensor.when_no_line = lambda:  drive_forward(enable1, enable2, pin1A, pin1B, pin2A, pin2B) #line

    ultra_sonic = gz.DistanceSensor(echo=8, trigger=11, threshold_distance=.1)
    ultra_sonic.when_in_range = lambda: drive_stop(enable1, enable2)

    signal.pause()

main()
