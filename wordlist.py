class Wordlist:
   def __init__(self):
      with open('diceware.wordlist.asc') as wordlist_file:
         self.wordlist_text = wordlist_file.read()

   def get(self, prefix):
      for line in self.wordlist_text.splitlines():
         if line.startswith(prefix):
            line_without_prefix_and_whitespace_padding = line[len(prefix):].strip()
            return line_without_prefix_and_whitespace_padding
      raise(LookupError('word lookup failed for key: ' + prefix))
            
