

import random   #import random module to get random numbers

print('Hi there! What is your name? ')
name = input()  #user name is stored in variable name

print('Hi ' +name + ' Guess a number between 1 and 20')
secretNumber = random.randint(1,20)

print('DEBUG secret number is ' + str(secretNumber))  # checks
    
while True:
    try:
        for guessesTaken in range(1,7):   # a range stored 1,7 stores values 1-6
            print('What is your guess? ')
            guess = int(input())
            if guess < secretNumber:
                        print('Your  guess is too low.')
            elif guess > secretNumber:
                         print('Your guess is too high.')
            else:
                break
        
        if guess == secretNumber:
            print('Great job, ' + name + '! You guessed the number in ' + str(guessesTaken) + ' guesses.')

        else:
            print('Alas. The secret number is ' + str(secretNumber))
        break
    except ValueError:
        print('You should enter a number. Start the game over')
