# Task username password

while True:
    print('Please type your username:')
    username = input()
    if username.isalnum():
        break
    print('Enter a username with numbers and letters')

while True:
    print('Select a pin')
    pin = input()
    if pin.isdecimal():
        break
    print('Please use numbers only')


