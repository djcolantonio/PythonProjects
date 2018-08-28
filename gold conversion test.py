#will convert g to ozT

while True:
    try:

        g = float(input('Enter the weight of gold in grams'))
        ozT = g * .032
        print(str(round(10, 2)) + ' g equals ' + str(round(ozT, 2)) + ' ozT.')
        if ozT >= 3:
            print('Accept')
        elif ozT <= 1:
            print('Reject')
        else:
            print('Correct')
    except ValueError:
        continue
    
