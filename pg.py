import random


input("This program generates easy-to-remember passwords by adding hints typed in by the user")
bruh = input("Enter a hint to be added to your password")

from nltk.corpus import wordnet

bruh2 = list(bruh)

ultrabruh = ['1','2','3','4','5','6','7','8','9','0']

lmfao = random.sample(ultrabruh, 4)
hints = []

synonyms = wordnet.synsets(bruh)
for ss in synonyms :
  if ss.name()[:len(ss.name())-4] not in hints :
     hints.append(ss.name()[:len(ss.name())-4])
  
hintsFinal = random.sample(hints, 2)

final = hintsFinal+lmfao

str1 = ''.join(final)

print("Password: ", str1)
#JS sux
#prawnie sux
