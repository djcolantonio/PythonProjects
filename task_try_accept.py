numCars = input('How many cars do you have? ')
try:
    if int(numCars) >=2:
        print ('Do you have a garage?')
    elif int(numCars) < 0:
        print('Enter a positive number')
    else:
        print('Do you park on the street')
except ValueError:
    print('Please enter a number.')
