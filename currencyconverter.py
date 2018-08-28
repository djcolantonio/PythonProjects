# This converts Euro in USD (current rate 1 Euro = 1.24USD)

Euro = float(input('Enter the Euro amount: '))
USD = Euro*1.24
print (str(round(Euro, 2)) + ' Euros equals ' + str(round(USD, 2)) + ' USD')
