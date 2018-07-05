import unittest
from unittest.mock import patch, call
from dicewareRoller import DicewareRoller
import random


class TestDicewareRoller(unittest.TestCase):
   @patch('dicewareRoller.Wordlist')
   @patch('dicewareRoller.Die')
   def test_diceware_roller(self, MockDie, MockWordlist):
      expected_word = 'hunter'
      expected_roll = random.randint(1,5)
      expected_key = str(expected_roll) * 5
      MockDie().roll.return_value = expected_roll
      MockWordlist().get.return_value = expected_word

      dicewareRoller = DicewareRoller()

      word = dicewareRoller.roll_one_word()

      self.assertEqual(word, expected_word)
      self.assertEqual(MockDie().roll.mock_calls,
            [call(), call(), call(), call(), call()])
      MockWordlist().get.assert_called_once_with(expected_key)

if __name__ == '__main__':
    unittest.main()
