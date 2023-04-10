import gpiozero as gz

class Motor:

    def __init__(self, pin_1, pin_2, pin_enable):
        print("you made a motor")
        self.digital_output_1 = gz.DigitalOutputDevice(pin_1)
        self.digital_output_2 = gz.DigitalOutputDevice(pin_2)
        self.pwm_output = gz.DigitalOutputDevice(pin_enable)



if __name__ == "__main__":
    print("You are running the file: rosebot_drivesystem")
    Motor_A_EN = 4
    Motor_B_EN = 17

    Motor_A_Pin1 = 14
    Motor_A_Pin2 = 15
    Motor_B_Pin1 = 27
    Motor_B_Pin2 = 18
    my_left_motor = Motor()