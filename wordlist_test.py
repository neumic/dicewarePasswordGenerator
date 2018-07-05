import unittest
from unittest.mock import patch
from unittest.mock import mock_open
from unittest.mock import call
from wordlist import Wordlist

mockWordlistText = """Ignore this line\n
\n
11111 Foo\n
12345 Bar\n
09876 Blat\n
somestring blaz\n
17456 ReturnMe\n
98765 NotMeee\n
"""

class TestWordlist(unittest.TestCase):
   def test_wordlist_happy(self):
      with patch('wordlist.open', mock_open(read_data=mockWordlistText)) as open_mock:
         wordlist = Wordlist()

         first_returned = wordlist.get('17456')
         self.assertEqual(first_returned, "ReturnMe")

         second_returned = wordlist.get('Ignore')
         self.assertEqual(second_returned, "this line")

         open_mock.assert_called_once_with("diceware.wordlist.asc")
         self.assertEqual(open_mock.mock_calls,
               [call('diceware.wordlist.asc'),
               call().__enter__(),
               call().read(),
               call().__exit__(None, None, None)])

   def test_wordlist_unhappy(self):
      with patch('wordlist.open', mock_open(read_data=mockWordlistText)) as open_mock:
         wordlist = Wordlist()
         invalidLookupKey = 'Not Found'

         with self.assertRaisesRegex(LookupError, 
               "word lookup failed for key: " + invalidLookupKey):
            wordlist.get(invalidLookupKey)
      
if __name__ == '__main__':
    unittest.main()
