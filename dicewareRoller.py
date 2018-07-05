from die import Die
from wordlist import Wordlist

class DicewareRoller:
   def roll_one_word(self):
      die = Die()
      wordlist = Wordlist()

      roll_string_list = [str(die.roll()) for count in range(5)]
      word_key = "".join(roll_string_list)

      return wordlist.get(word_key)

