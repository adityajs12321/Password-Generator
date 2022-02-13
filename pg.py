import random
import tkinter
from nltk.corpus import wordnet

mac = tkinter.Tk()
mac.title('Password Generator')
mac.geometry('450x300')

def DeleteEntry() :
  b.destroy()
  c.destroy()

def true():
  global c
  global b
  c = tkinter.Button(mac, text='Delete Entry', command = DeleteEntry)
  c.place(x=90, y=60)
  global b
  print("Working")
  inp = inputtxt.get(1.0, 'end-1c')
  tkinter.Label(mac, text=inp).place(x=10, y=10)
  print(inp)

  numbers = ['1','2','3','4','5','6','7','8','9','0']

  randomized = random.sample(numbers, 4)
  global hints
  hints = []

  synonyms = wordnet.synsets(inp)
  for ss in synonyms :
    if ss.name()[:len(ss.name())-4] not in hints :
       hints.append(ss.name()[:len(ss.name())-4])
  if len(hints) > 1:
    hintsFinal = random.sample(hints, 2)
  else :
    hintsFinal = hints

  final = hintsFinal+randomized

  str1 = ''.join(final)
  hmm = 'Password: ' + str1
  b = tkinter.Label(mac, text=hmm)
  b.place(relx=0.5, rely=0.75, anchor='center')
  
tkinter.Label(mac, text='Enter a hint to be added to your password').place(x=10, y=40)
inputtxt = tkinter.Text(mac, height = 1, width =20)
inputtxt.place(relx = 0.78, rely = 0.18,anchor = 'center')
tkinter.Button(mac, text='Enter', command = true).place(x=10,y=60)



#JS sux
#prawnie sux
tkinter.mainloop()
