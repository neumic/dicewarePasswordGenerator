import random

class Die:
   def __init__(self):
      self.system_random = random.SystemRandom()

   def roll(self):
      return self.system_random.randint(1,6)
