from argparse import ArgumentParser
from dicewarePasswordGenerator import DicewarePasswordGenerator

def main():
   argumentParser = ArgumentParser(description="Generates a simple password from a diceware password file.  The file must be named 'diceware.wordlist.asc'")
   argumentParser.add_argument('word_count', type=int, help='The number of words the password will contain')
   arguments = argumentParser.parse_args()
   generator = DicewarePasswordGenerator()
   print(generator.generate_simple_password(arguments.word_count))

if __name__ == '__main__':
   main()

