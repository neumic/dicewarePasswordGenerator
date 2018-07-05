from dicewareRoller import DicewareRoller

class DicewarePasswordGenerator:
   def generate_simple_password(self, number_of_words):
      roller = DicewareRoller()

      list_of_words = [roller.roll_one_word() for count in range(number_of_words)]

      return "".join(list_of_words)

