from random import randint
from os import system
import platform

def clear():
  return system("cls") if platform.system() == 'Windows' else system("clear")

def print_gallows(errors, lines = []):
  print("=" * 7)

  col = "||"
  print(col + "    |")
  print(col + "    |")

  if errors == 1:
    lines[0] = col + "    O"
  if errors == 2:
    lines[1] = col + "    |"
  if errors == 3:
    lines[0] = col + "   \O"
  if errors == 4:
    lines[0] = col + "   \O/"
  if errors == 5:
    lines[2] = col + "   /"
  if errors == 6:
    lines[2] = col + "   / \\"
  
  for line in lines:
    if line:
      print(line)
    else:
      print(col)
  print(col)
  
  return lines

words = [
  "banana", "melancia", "abacaxi",
  "uva", "acerola", "cupuacu",
  "morango", "limao", "nectarina",
  "abacate", "pera", "pitanga",
  "manga", "jabuticaba",
]

word = {}
word['word'] = words[randint(0, len(words) - 1)]
word['letters'] = [l for l in word['word']]
word['len_word'] = len(word['letters'])
word['hidden'] = "_ " * word['len_word']

list_tries = ["_" for i in range(word['len_word'])]
aux_list = [ "_ " for i in range(word['len_word'])]

clear()
print("\n" * 10)

errors = [0, ["||", "||","||"], ""]

while True:
  typed = False

  tries = input("Try hit some letter: ")
  
  if tries.lower() in errors[2]:
    errors[1] = print_gallows(errors[0], errors[1])
    typed = True
  elif tries not in word['letters']:
    errors[0] += 1
  errors[2] += tries.lower() if tries.lower() not in errors[2] else ""  
  
  for i in range(word['len_word']):
    if word['letters'][i] != tries and list_tries[i] != "_":
      aux_list[i] = f"{list_tries[i].upper()} " 
    elif word['letters'][i] == tries:
      list_tries[i] = tries.upper()
      aux_list[i] = tries.upper() + " "

  word["hidden"] = "".join(aux_list)
  clear()
  print("\n" * 10)
  print(word["hidden"])
  errors[1] = print_gallows(errors[0], errors[1])
  print("This Letter's Already Typed ! ! !" if typed else "")

  if errors[0] > 6:
    print("\n" * 10)
    print("=" * 50, end="\n")
    print("\n" * 5)
    print("{}".format("YOU DIED".center(50)))
    print("\n" * 5)
    print("=" * 50, end="\n")
    print("\n" * 6)
    break

  if "_ " not in word['hidden']:
    print("\n" * 10)
    print("=" * 50, end="\n")
    print("\n\n")
    print(((" " * 9) + "*") * 4 + "\n\n")
    print("{}".format("YOU WIN".center(50)))
    print("\n\n")
    print(((" " * 9) + "*") * 4 + "\n\n")
    print("=" * 50, end="\n")
    print("\n" * 6)
    break
