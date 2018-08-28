import random

input('Enter your question, and I will tell your fortune ')

messages = ['It is certain', 'It is decidedly so', 'Yes, definitely', 'Hazy, try again', 'Ask again later', 'Focus and ask again', 'My reply is no', 'Outlook is not so good']
print(messages[random.randint (0, len(messages) - 1)])
