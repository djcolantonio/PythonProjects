courses = []
print('Enter courses that you take this semester ')
while True:
    print('Enter course ' + str(len(courses)+1) + ' or press Enter to stop')
    course = input()
    if course == '':
        break
    courses = courses + [course]
print ('My courses are: ')
for course in courses:
    print(' ' + course)
