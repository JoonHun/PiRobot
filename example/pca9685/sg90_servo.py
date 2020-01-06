from __future__ import division
import time

# PCA9685모듈을 임포트.
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685() #pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# min 80, mid 320, max 560
servo_min = 80  # -90
servo_mid = 300  # 0
servo_max = 520  # 90

pwm.set_pwm_freq(50)

# 서보 펄스폭을 더 간단하게 만들어주는 함수.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 50 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    print('{0} pulse'.format(pulse))
    pwm.set_pwm(channel, 0, pulse)

while True:
#    pwm.set_pwm(15, 0, servo_mid)
#    print(servo_mid)
#    time.sleep(1) # 1초정지.

#    for value in range(80, 70, -1):
#        pwm.set_pwm(15, 0, value)
#        print(value)
#        time.sleep(1) # 1초정지.

    pwm.set_pwm(0, 0, servo_mid)
    print(servo_mid)
    time.sleep(1) # 1초정지.
    pwm.set_pwm(0, 0, servo_min)
    print(servo_min)
    time.sleep(1) # 1초정지.
    pwm.set_pwm(0, 0, servo_mid)
    print(servo_mid)
    time.sleep(1) # 1초정지.
    pwm.set_pwm(0, 0, servo_max)
    print(servo_max)
    time.sleep(1) # 1초정지.

