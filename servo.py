from machine import Pin, PWM
import pins

SERVO_UNLOCK = 0
SERVO_LOCK = 90

MIN_DUTY = 1802
MAX_DUTY = 7864
def angle_to_duty(angle):
    return int(MIN_DUTY + (angle / 180) * (MAX_DUTY - MIN_DUTY))

#####

servo = PWM(Pin(pins.SERVO))
servo.freq(50)

def set_servo_angle(angle):
    if 0 <= angle <= 180:
        duty = angle_to_duty(angle)
        servo.duty_u16(duty)
        print(f"{servo} - {angle} degrees")

def Unlock():
    set_servo_angle(SERVO_UNLOCK)
def Lock():
    set_servo_angle(SERVO_LOCK)