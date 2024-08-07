from machine import Pin, PWM
from utime import sleep

BUZZER_PIN = 27
buzzer = PWM(Pin(BUZZER_PIN))

def buzz(frequency, duration, duty_cycle):
    buzzer.freq(frequency)
    buzzer.duty_u16(duty_cycle)
    sleep(duration)
    buzzer.duty_u16(0)

def UnlockSound():
    buzz(frequency=1000, duration=0.2, duty_cycle=32768)

def LockSound():
    buzz(frequency=500, duration=0.2, duty_cycle=32768)

def InvalidSound():
    buzz(frequency=2000, duration=0.2, duty_cycle=32768)
    sleep(0.1)
    buzz(frequency=2000, duration=0.2, duty_cycle=32768)
    sleep(0.1)
    buzz(frequency=2000, duration=0.2, duty_cycle=32768)
