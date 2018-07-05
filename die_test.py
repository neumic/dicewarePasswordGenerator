import unittest
import unittest.mock
from die import Die

class TestDie(unittest.TestCase):
   def test_die_functional(self):
      die = Die()
      for roll in range(100):
         value = die.roll()
         checkRoll(self, value)

   @unittest.mock.patch('die.random')
   def test_die_mocked_random(self, randomMock):
      expectedRandomNumber = 4
      mockSysRandom = randomMock.SystemRandom()
      mockSysRandom.randint.return_value=expectedRandomNumber
      
      die = Die()
      value = die.roll()

      self.assertEqual(value,expectedRandomNumber)
      mockSysRandom.randint.assert_called_once_with(1,6)

      anotherDifferentNumber=18
      mockSysRandom.randint.reset_mock()
      mockSysRandom.randint.return_value=anotherDifferentNumber

      value = die.roll()

      self.assertEqual(value,anotherDifferentNumber)
      mockSysRandom.randint.assert_called_once_with(1,6)
      

def checkRoll(test, value):
   test.assertTrue(value>=1)
   test.assertTrue(value<=6)

if __name__ == '__main__':
    unittest.main()
