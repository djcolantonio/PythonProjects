# this program asks a user his username and password

while True:
    name = input('Enter the username:  ')
    if name != 'djcolantonio':
        continue
    print('Hello ' + name + '!' + ' Enter your password. (Hint: It is a dog.)')

    while True:
        password = input()
        if password == 'hazel':
            break
        else:
            print('Password does not match.  Please enter your password again.')
            
    print('Access Granted ' + name)
    break
