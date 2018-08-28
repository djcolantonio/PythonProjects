# This program says Hello and asks for my name and age 
print('Hi there!')
print('What is your name?') # ask for their name
myName = input()
print('Pleasure to meet you, ' + myName) # the program responds with a name
print('The length of your name is:')
print(len(myName))
print('How old are you?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge)+1) + ' in a year.')
