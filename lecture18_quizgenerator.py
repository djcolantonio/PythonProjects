import random

myQuiz = {'What city does the NBA team "Hornets" reside in?' : 'charlotte',
          'Who is the starting point guard for the Charlotte Hornets?' :'Kemba Walker',
          'The New Orleans Pelicans was recently created in the 2000s. What team was in New Orleans before them?' : 'hornets',
          'Who is the starting center for the New York Knicks?' : 'kristaps porzingis',
          'Who won 3 championships with the Miami HEAT?' : 'Dwyane Wade'}

print('Please take this quiz')
print('=====================')

while True:
    myLoopQuiz = myQuiz.copy()
    score = 0
    
    num = int(input('''How many questions would you like?
Choose between 1-{max} '''.format(max = len(myLoopQuiz)))) 
    if num < 1 or num > len(myLoopQuiz):
        print("Error: choose between 1 and {max}".format(max = len(myLoopQuiz)))
        continue

    for i in range (num):
        question = random.choice(list(myLoopQuiz.keys()))
        answer = myLoopQuiz.pop(question)

        print('\nQuestion ' + str(i+1))
        print(question)

        guess = input (' > ')

        if guess.lower()== answer.lower():
            print('Correct!')
            score += 1
        else:
            print('Sorry, wrong answer')
    
    print('\nYour final score is ' + str(score))
    playAgain = input('Would you like to play agin? Type Yes or No. ')
    if playAgain.lower() == 'yes':
        continue
    else:
        break
        
