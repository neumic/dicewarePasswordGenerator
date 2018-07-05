import unittest
from unittest.mock import patch
from dicewarePasswordGenerator import DicewarePasswordGenerator
import random

class TestDicewarePasswordGenerator(unittest.TestCase):

   @patch('dicewarePasswordGenerator.DicewareRoller')
   def test_generate_simple_password(self, mockRoller):
      number_of_words = random.randint(1,7)
      word_to_return = "bird" + str(random.randint(1,4))
      mockRoller().roll_one_word.return_value = word_to_return

      generator = DicewarePasswordGenerator()
      password = generator.generate_simple_password(number_of_words)

      self.assertEqual(len(mockRoller().roll_one_word.mock_calls), number_of_words)
      self.assertEqual(password, word_to_return * number_of_words)

if __name__ == '__main__':
   unittest.main()
