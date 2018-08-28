# This will convert yuan into USD

Yuan = float(input('Enter the Yuan amount: '))
USD = Yuan*.16
print (str(round(Yuan, 2)) + ' Yuan equals ' + str(round(USD, 2)) + ' USD')
if USD == 100:
    print('it\'s just right')
elif USD > 100:
    print('it\'s a lot')
elif USD < 100:
    print('it is too little')

