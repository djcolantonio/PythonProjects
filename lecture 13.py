while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number.')

while True:
    print('''Select a new password. Use letters and numbers only: ''')
    password = input()
    if password.isalnum():
        break
    print('Passwords can have only letters and nummbers')
