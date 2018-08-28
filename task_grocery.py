groceries = []
print('Enter your shopping list ')
while True:
    print('Enter grocery item ' + str(len(groceries)+1) + ' or press Enter to stop')
    grocery = input()
    if grocery == '':
        break
    groceries = groceries + [grocery]
print ('My groceries list: ')
for grocery in groceries:
    print(' ' + grocery)
