import time

import Adafruit_PCA9685
import RPi.GPIO as GPIO

MAX_SPEED = 4096
MID_SPEED = 2500
LOW_SPEED = 1500

Motor0_A = 11  # pin11
Motor0_B = 12  # pin12
Motor1_A = 13  # pin13
Motor1_B = 15  # pin15

EN_M0    = 4  # servo driver IC CH4
EN_M1    = 5  # servo driver IC CH5

pins = [Motor0_A, Motor0_B, Motor1_A, Motor1_B]

pwm = Adafruit_PCA9685.PCA9685()

def setSpeed(speed):
	print("speed is: {}".format(speed))
	pwm.set_pwm(EN_M0, 0, speed)
	pwm.set_pwm(EN_M1, 0, speed)

# x = 0 : stop , x = 1 : forward , X = 2 : backward
def motorRight(x):
    if x == 0:
        GPIO.output(Motor0_A, GPIO.LOW)
        GPIO.output(Motor0_B, GPIO.LOW)
    elif x == 1:
        GPIO.output(Motor0_A, GPIO.HIGH)
        GPIO.output(Motor0_B, GPIO.LOW)
    elif x == 2:
        GPIO.output(Motor0_A, GPIO.LOW)
        GPIO.output(Motor0_B, GPIO.HIGH)	
    else:
        print('Config Error')

# x = 0 : stop , x = 1 : forward , X = 2 : backward
def motorLeft(x):
    if x == 0:
        GPIO.output(Motor1_A, GPIO.LOW)
        GPIO.output(Motor1_B, GPIO.LOW)
    elif x==1:
        GPIO.output(Motor1_A, GPIO.LOW)
        GPIO.output(Motor1_B, GPIO.HIGH)
    elif x == 2:
        GPIO.output(Motor1_A, GPIO.HIGH)
        GPIO.output(Motor1_B, GPIO.LOW)
    else:
        print('Config Error')

def stop():
#	for pin in pins:
#		GPIO.output(pin, GPIO.LOW)
    motorLeft(0)
    motorRight(0)

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

    setSpeed(MID_SPEED)

def forward(speed):
    setSpeed(speed)
    motorRight(1)
    motorLeft(1)

def backward(speed):
    setSpeed(speed)
    motorRight(2)
    motorLeft(2)

# direction = 1 : Left, Direction = 2 : Right
def tankTurn(direction, angle):
    if direction == 1:
        motorLeft(2)
        motorRight(1)
    elif direction == 2:
        motorLeft(1)
        motorRight(2)
    else:
        print('Config Error')
        return
    
    delay = angle / 90.0 / 2.0
    print("delay {:f}".format(delay))

    time.sleep(delay)
    stop()


if __name__ == '__main__':
    setup()

    tankTurn(1,90)
    time.sleep(1)

    forward(MID_SPEED)
    time.sleep(2)
    stop()
    time.sleep(1)

    backward(MID_SPEED)
    time.sleep(2)
    stop()
    time.sleep(1)

"""
    setSpeed(LOW_SPEED)
    motor0('True')
    time.sleep(2)
    motor0('False')
    time.sleep(2)

    motor1('True')
    time.sleep(2)
    motor1('False')
    time.sleep(2)

    stop()
"""
