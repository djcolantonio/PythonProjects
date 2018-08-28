# This program evaluates the score and LOOPS

while True:
    score = input('What is your score: ')
    try:
        if int(score) >= 90:
            print('This is an excellent score')
        elif int(score) >=80:
            print('This is a good score')
        else:
            print('You need a better score')
        break
    except ValueError:
        print('Please enter a number')
