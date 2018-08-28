while True:
    try:
        year = int(input('Enter your birth year: '))

        yearNumber = (year - 2000) % 12 

        zodiac = ['Dragon', 'Snake', 'Horse', 'sheep', 'monkey', 'rooster', 'dog', 'pig', 'rat', 'ox', 'tiger', 'hare']

        print('Your sign is ' + zodiac(yearNumber))
        askAgain = input('Would you like to try again')
        if askAgain == 'yes':
            continue
        else:
            break
        
    except ValueError:
        print('Please enter a number')
