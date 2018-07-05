import unittest
from unittest.mock import patch, call
import commandline
import argparse

class TestCommandLineInterface(unittest.TestCase):
   @patch('commandline.DicewarePasswordGenerator')
   @patch('commandline.ArgumentParser')
   @patch('commandline.print')
   def testArgParserCalls(self,mockPrint, mockArgumentParser, mockDicewareGenerator):
      expectedWordCount = 45
      expectedArgs = argparse.Namespace(word_count=expectedWordCount)
      expectedPassword = 'password'
      mockArgumentParser().parse_args.return_value = expectedArgs
      mockDicewareGenerator().generate_simple_password.return_value = expectedPassword

      commandline.main()

      self.assertEqual(mockArgumentParser.mock_calls, 
         [call(),call( description="Generates a simple password from a diceware password file.  The file must be named 'diceware.wordlist.asc'"),
          call().add_argument('word_count', type=int, help='The number of words the password will contain'),
          call().parse_args()])
      mockDicewareGenerator().generate_simple_password.assert_called_once_with(expectedWordCount)
      mockPrint.assert_called_once_with(expectedPassword)


if __name__ == '__main__':
   unittest.main()

