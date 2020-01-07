import time

import Adafruit_PCA9685
import RPi.GPIO as GPIO

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

def motor0(x):
	if x == 'True':
		GPIO.output(Motor0_A, GPIO.LOW)
		GPIO.output(Motor0_B, GPIO.HIGH)
	elif x == 'False':
		GPIO.output(Motor0_A, GPIO.HIGH)
		GPIO.output(Motor0_B, GPIO.LOW)
	else:
		print('Config Error')

def motor1(x):
	if x == 'True':
		GPIO.output(Motor1_A, GPIO.LOW)
		GPIO.output(Motor1_B, GPIO.HIGH)
	elif x == 'False':
		GPIO.output(Motor1_A, GPIO.HIGH)
		GPIO.output(Motor1_B, GPIO.LOW)
	else:
		print('Config Error')

def stop():
	for pin in pins:
		GPIO.output(pin, GPIO.LOW)

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

if __name__ == '__main__':
    setup()
    setSpeed(4095)
    motor0('True')
    time.sleep(2)
    motor0('False')
    time.sleep(2)
    stop()
