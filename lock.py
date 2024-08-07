import servo
import buzzer
import screen
import keypad

from utime import sleep

MAX_TRIES = 3
RETRY_WAIT_TIME = 60
CODE = "123456"

def Unlock():
  screen.Write("Unlocking...")
  buzzer.UnlockSound()
  sleep(0.5)
  servo.Unlock()
  screen.Write("[UNLOCKED]")

def Lock():
  screen.Write("Locking...")
  buzzer.LockSound()
  sleep(0.5)
  servo.Lock()
  screen.Write("[LOCKED]")

  sleep(2)
  screen.Write("Press key to")
  screen.Write("enter code", False, 0, 10)

def PromptForCode():
    screen.Write("Enter code:")
    screen.Write()
    entered_code = ""
    attempts = 0
    
    while attempts < MAX_TRIES:
        key = keypad.GetKey()
        if key is not None:
            if key == '#':
                if entered_code == CODE:
                    Unlock()
                    return True
                else:
                    attempts += 1
                    screen.Write("Incorrect!")
                    screen.Write(f"Attempt {attempts}/{MAX_TRIES}", False, 0, 10)

                    buzzer.InvalidSound()
                    sleep(3)
                    
                    if attempts < MAX_TRIES:
                        screen.Write("Wrong code. Try again:")
                        entered_code = ""
                    else:
                        screen.Write("Max tries reached. Waiting...")
                        buzzer.InvalidSound()
                        sleep(RETRY_WAIT_TIME)
                        return False
            elif key == '*':  # Assuming '*' is used to clear the code
                entered_code = ""
                screen.Write("Code Cleared")
                sleep(1)  # Brief pause before clearing the display
                screen.Write("Enter Code:")
            else:
                entered_code += key
                screen.Write(f"Code: {entered_code}")
                
    return False