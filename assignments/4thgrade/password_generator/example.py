# Random jingle/note Generator
# Free draw? (explanation needed)
# personality quiz 
# who will your teacher be?
# What your future job would be (quiz)
# Self Writing Story (Would have to create)
# Spell checker
# Random letter/password Generator


import random


password = ''
for l in range(1, 9):
  num = random.randint(1, 41)

  if num == 1:
    # print('a')
    password = password + 'a'
  elif num == 2:
    # print('b')
    password = password + 'b'
  elif num == 3:
    # print('c')
    password = password + 'c'
  elif num == 4:
    #print('d')
    password = password + 'd'
  elif num == 5:
    print('e')
  elif num == 6:
    print('f')
  elif num == 7:
    print('g')
  elif num == 8:
    print('h')
  elif num == 9:
    print('i')
  elif num == 10:
    print('j')
  elif num == 11:
    print('k')
  elif num == 12:
    print('l')
  elif num == 13:
    print('m')
  elif num == 14:
    print('n')
  elif num == 15:
    print('o')
  elif num == 16:
    print('p')
  elif num == 17:
    print('q')
  elif num == 18:
    print('r')
  elif num == 19:
    print('s')
  elif num == 20:
    print('t')
  elif num == 21:
    print('u')
  elif num == 22:
    print('v')
  elif num == 23:
    print('w')
  elif num == 24:
    print('x')
  elif num == 25:
    print('y')
  elif num == 26:
    print('z')
  elif num == 27:
    print('!')
  elif num == 28:
    print('@')
  elif num == 29:
    print('#')
  elif num == 30:
    print('$')
  elif num == 31:
    print('*')
  elif num == 32:
    print('1')
  elif num == 33:
    print('2')
  elif num == 34:
    print('3')
  elif num == 35:
    print('4')
  elif num == 36:
    print('5')
  elif num == 37:
    print('6')
  elif num == 38:
    print('7')
  elif num == 39:
    print('8')
  elif num == 40:
    print('9')
  elif num == 41:
    print('0')
  else:
    print(num)

print('Your password is: ' + password)