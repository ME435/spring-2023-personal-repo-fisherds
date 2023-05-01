import gpiozero as gz
import time
import signal

# Make digital output devices for the motor pins
pinLA = gz.DigitalOutputDevice(27)
pinLB = gz.DigitalOutputDevice(18)
enableL = gz.PWMOutputDevice(17)

pinRA = gz.DigitalOutputDevice(14)
pinRB = gz.DigitalOutputDevice(15)
enableR = gz.PWMOutputDevice(4)

# Sensor Pins
line_pin_left = 19
line_pin_middle = 16
line_pin_right = 20
ultrasonic_pin_echo = 8
ultrasonic_pin_trigger = 11

# Create Sensor gz Objects
left_line_sensor = gz.LineSensor(line_pin_left)
middle_line_sensor = gz.LineSensor(line_pin_middle)
right_line_sensor = gz.LineSensor(line_pin_right)
ultrasonic_sensor = gz.DistanceSensor(ultrasonic_pin_echo, ultrasonic_pin_trigger)

def main():
    print("Line Following")
    while True:
        # Get sensor outputs
        distance = getUSDistanceInCm()
        lineSensorOutputs = getLineSensorOutputs()

        # Print sensor outputs to terminal
        print("Distance: ", distance)
        print("L M R: ", lineSensorOutputs)

        # Motor behavior based on sensor readings
        if distance < 20:
            # stop motors
            print("Obstacle! Stop Motors")
            stopMotors()
        elif lineSensorOutputs == [0, 1, 0]:
            # in middle: both motors forward
            print("Go forwards")
            forward(0.5)
        elif lineSensorOutputs == [1, 1, 0]:
            # turn slightly left: left motor reverse slow, keep right motor on at high speed
            print("Slight left turn")
            turnLeft(0.25, 0.5)
        elif lineSensorOutputs == [1, 0, 0]:
            # turn hard left: left motor reverse high, keep right motor on at high speed
            print("Sharp left turn")
            turnLeft(0.5, 0.5)
        elif lineSensorOutputs == [0, 1, 1]:
            # turn slightly right: right motor reverse slow, keep left motor on at high speed
            print("Slight right turn")
            turnRight(0.5, 0.25)
        elif lineSensorOutputs == [0, 0, 1]:
            # turn hard right: right motor reverse high, keep left motor on at high speed
            print("Sharp right turn")
            turnRight(0.5, 0.5)
        else:
            # stop motors
            print("Stop Motors")
            stopMotors()

        time.sleep(0.1)

def stopMotors():
    pinRA.off()
    pinRB.off()
    enableR.value = 0.0

    pinLA.off()
    pinLB.off()
    enableL.value = 0.0

def backward(motorSpeed):
    pinRA.on()
    pinRB.off()
    enableR.value = motorSpeed

    pinLA.off()
    pinLB.on()
    enableL.value = motorSpeed

def forward(motorSpeed):
    pinRA.off()
    pinRB.on()
    enableR.value = motorSpeed

    pinLA.on()
    pinLB.off()
    enableL.value = motorSpeed

def turnRight(leftMotorSpeed, rightMotorSpeed):
    pinRA.on()
    pinRB.off()
    enableR.value = rightMotorSpeed

    pinLA.on()
    pinLB.off()
    enableL.value = leftMotorSpeed

def turnLeft(leftMotorSpeed, rightMotorSpeed):
    pinRA.off()
    pinRB.on()
    enableR.value = rightMotorSpeed

    pinLA.off()
    pinLB.on()
    enableL.value = leftMotorSpeed

def getUSDistanceInCm():
    return ultrasonic_sensor.distance * 100

def getLineSensorOutputs():
    # black is a value of 1, white is a value of 0
    return [left_line_sensor.value, middle_line_sensor.value, right_line_sensor.value]


main()
