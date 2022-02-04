import subprocess

def module_installation() :
  subprocess.run(['pip', 'install', 'nltk'])

module_installation()

import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet
