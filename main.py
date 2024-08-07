import servo
import buzzer
import screen
import keypad
import lock

from math import floor
from utime import sleep
import time

def Welcome():
  screen.Write("Lock initialized")
  sleep(0.5)
  lock.Lock()

Welcome()

lastKey = time.time()
while True:
    key = keypad.GetKey()
    if key is None:
        current = time.time()
        remaining = floor(current - lastKey)

        screen.Write("[LOCKED]")
    else:
        if lock.PromptForCode():
            screen.Write("Press key to")
            screen.Write("lock", False, 0, 10)
            screen.Write(f"Auto-lock: {remaining}s", False, 0, 20)

            key = keypad.GetKey()
            if key is not None:
                Lock()
        else:
            # System locked after max retries
            screen.Write("System locked. Waiting...")
            sleep(lock.RETRY_WAIT_TIME)

    sleep(1)