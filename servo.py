from machine import Pin, PWM

SERVO_PIN = 14
SERVO_UNLOCK = 90
SERVO_LOCK = 0

MIN_DUTY = 1802
MAX_DUTY = 7864
def angle_to_duty(angle):
    return int(MIN_DUTY + (angle / 180) * (MAX_DUTY - MIN_DUTY))

#####

servo = PWM(Pin(SERVO_PIN))
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