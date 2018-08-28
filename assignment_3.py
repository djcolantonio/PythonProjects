numScore = input('What was your score? ')
try:
    if int(numScore) >=90:
        print ('You are an excellent student!')
    elif int(numScore) >=80:
        print('You are a very good student')
    else:
        print('You need a good score on the exam')
except ValueError:
    print('Please enter an integer.')
