numCars = input('How many cars do you have? ')
try:
    if int(numCars) >=2:
        print ('Do you have a garage?')
    else:
        print('Do you park on the street')
except ValueError:
    print('Please enter a number')
