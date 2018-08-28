dayslist = ['Monday', 'Tuesday', 'Wednesday', 'Tuesday', 'Wednesday', 'Friday']
unwanted = {'Tuesday', 'Wednesday'}
dayslist2 = [x for x in dayslist if x not in unwanted]
