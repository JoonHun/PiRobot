from __future__ import division
import time

# PCA9685모듈을 임포트.
import Adafruit_PCA9685


pwm = Adafruit_PCA9685.PCA9685() #pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# experimental value min 80, mid 320, max 560
# 50 hz => 20ms
# 20 ms / 4096 (12bit resolution) = 4.88 us
# just calcurated value
#  90 : 1 ms   => 1000 / 4.88 = 205   
#   0 : 1.5 ms => 1500 / 4.88 = 308   
# -90 : 2 ms   => 2000 / 4.88 = 410   
# experimental value 
#  90 : 120
#   0 : 340
# -90 : 560

SERVO_VAL = [340, 120, 340, 560]

pwm.set_pwm_freq(50)

"""
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
"""

while True:
    servo_num = input("select servo 0 , 14, 15 : ")
    SERVO = int(servo_num, 10)
    print("select servo {:2d}".format(SERVO))
    Val = 340
    pwm.set_pwm(SERVO, 0, Val)
    flag = True

    while flag:
        di = input("select directorion 1(left) , 3(right) , 0(exit) : ")
        print("select key {}".format(di))
        
        if(di == "0" ):
            flag = False
        elif(di == "1"):
            Val += 20 
        else:
            Val -= 20

        pwm.set_pwm(SERVO, 0, Val)
        print("servo %2d = %d"%(SERVO, Val))



"""
while True:
    for val in SERVO_VAL:
        for servo in SERVO:
            pwm.set_pwm(servo, 0, val)
            print("servo %2d = %d"%(servo, val))
        time.sleep(3)
    
"""
