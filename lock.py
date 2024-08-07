import servo
import buzzer
import screen
import keypad

from utime import sleep
import time

MAX_TRIES = 3
RETRY_WAIT_TIME = 60
CODE = "123456"
AUTOLOCK_TIME = 30

class LockSystem:
  def __init__(self):
    self.locked = False
    self.locking = False
    self.attempts = 0
    self.entered_code = ""
    self.last_interaction_time = time.time()

  def unlock(self):
    if self.locking:
      return

    self.locking = True
    screen.Write("Unlocking...")
    buzzer.UnlockSound()
    servo.Unlock()
    screen.Write("[UNLOCKED]")
    
    self.locked = False
    self.locking = False

    self.u()

  def lock(self):
    if self.locking:
      return
    
    self.locking = True
    screen.Write("Locking...")
    buzzer.LockSound()
    servo.Lock()
    self.locked = True
    self.locking = False

    screen.Write("Press key to")
    screen.Write("enter code", False, 0, 10)

    self.u()

  def screen_code_prompt(self):
    screen.Write("Enter code:")
    prompt = "[" + "*" * len(self.entered_code) + "_" * (6 - len(self.entered_code)) + "]"
    screen.Write(prompt, False, 0, 10)

  def display_autolock_countdown(self, remaining):
    if remaining > 0:
      screen.Write(f"Autolocking in {int(remaining_time)}s", False, 0, 10)
    else:
      screen.Write("Autolocking now!", False, 0, 10)

  def check_autolock(self):
    current = time.time()
    if not self.locked and (current - self.last_interaction_time) > AUTOLOCK_TIME:
      self.lock()

    remaining = AUTOLOCK_TIME - (current - self.last_interaction_time)
    self.display_autolock_countdown(remaining)

  def u(self):
    self.last_interaction_time = time.time()

  def get_code(self):
    self.screen_code_prompt()
    self.u()
    while self.attempts < MAX_TRIES:
      key = keypad.GetKey()
      if key is None:
        sleep(0.01)
        continue
      
      self.screen_code_prompt()
      
      if key == "#":
        if self.entered_code == CODE:
          self.attempts = 0
          self.entered_code = ""
          self.unlock()
        else:
          self.attempts += 1
          screen.Write("Incorrect code!")
          screen.Write(f"Attempt {self.attempts}/{MAX_TRIES}", False, 0, 10)
          self.entered_code = ""

          buzzer.InvalidSound()
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

  def prompt_for_code(self):
    if self.locking:
      print("Currently locking!")
      return
    if not self.locked:
      print("Currently unlocked!")
      return
    
    self.get_code()