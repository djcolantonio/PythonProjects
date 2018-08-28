# Guess the number between 1 and 10

import random
targetNum = random.randint (1,10)
guessNum = random.randint (1,10)

while targetNum != guessNum:
    guessNum = int(input('Guess a number between 1 and 10 until you get it right '))
print('You got it!')
                         
