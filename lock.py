import servo
import buzzer
import screen
import keypad

from utime import sleep
import time

MAX_TRIES = 3
RETRY_WAIT_TIME = 60
CODE = "123456"
AUTOLOCK_TIME = 5

class LockSystem:
  def __init__(self):
    self.locked = False
    self.locking = False
    self.attempts = 0
    self.entered_code = ""
    self.last_interaction_time = time.time()

  def reset_state(self):
    self.entered_code = ""
    self.attempts = 0

  def unlock(self):
    if self.locking:
      return

    print("Unlocking...")
    self.reset_state()

    self.locking = True
    screen.Write("Unlocking...")
    buzzer.UnlockSound()
    servo.Unlock()
    screen.Write("[UNLOCKED]", True, None, None, 0, -15)
    screen.Write("[#] to lock", False, None, None, 0, 5)
    screen.Write("Autolock after", False, None, None, 0, 15)
    screen.Write(f"{AUTOLOCK_TIME}s", False, None, None, 0, 25)

    self.locked = False
    self.locking = False

    self.u()

  def lock(self):
    if self.locking:
      return
    
    print("Locking...")
    self.reset_state()
    
    self.locking = True
    screen.Write("Locking...")
    buzzer.LockSound()
    servo.Lock()
    self.locked = True
    self.locking = False

    self.start_lock_prompt()
    self.u()

  def start_lock_prompt(self):
    screen.Write("[LOCKED]", True, None, None, 0, -15)

    screen.Write("Press key to", False, None, None, 0, -5)
    screen.Write("enter code", False, None, None, 0, 5)

  def screen_code_prompt(self):
    screen.Write("Enter code:", True, None, None, 0, -5)
    prompt = "[" + "*" * len(self.entered_code) + "_" * (6 - len(self.entered_code)) + "]"
    screen.Write(prompt, False, None, None, 0, 5)

  def display_autolock_countdown(self, remaining):
    if remaining <= 0:
      screen.Write("Autolocking!")
      sleep(1)

  def check_autolock(self):
    current = time.time()
    if self.locked == True:
      return

    if (current - self.last_interaction_time) > AUTOLOCK_TIME:
      self.lock()
      sleep(2)

    remaining = AUTOLOCK_TIME - (current - self.last_interaction_time)
    self.display_autolock_countdown(remaining)

  def u(self):
    self.last_interaction_time = time.time()
  
  def check_key(self, key):
    if key == "#":
      if self.entered_code == CODE:
        self.attempts = 0
        self.unlock()
        return True
      else:
        self.attempts += 1
        screen.Write("Incorrect code!", True, None, None, 0, -5)
        screen.Write(f"Attempt {self.attempts}/{MAX_TRIES}", False, None, None, 0, 5)

        self.entered_code = ""

        buzzer.InvalidSound()
        if self.attempts == MAX_TRIES:
          sleep(RETRY_WAIT_TIME)

        sleep(3)
        self.screen_code_prompt()
    elif key == "*":
      self.entered_code = ""
      screen.Write("Code cleared!")
      sleep(0.5)
      self.screen_code_prompt()
    else:
      self.entered_code += key
      self.screen_code_prompt()

  def get_code(self):
    self.screen_code_prompt()
    self.u()
    while self.attempts < MAX_TRIES:
      key = keypad.GetKey()
      if key is None:
        sleep(0.01)
        continue
      
      self.screen_code_prompt()
      result = self.check_key(key)
      if result:
        break

  def prompt_for_code(self, key):
    if self.locking:
      print("Currently locking!")
      return
    if not self.locked:
      print("Currently unlocked!")
      return

    if key != "*" and key != "#":
      self.entered_code += key
    self.get_code()