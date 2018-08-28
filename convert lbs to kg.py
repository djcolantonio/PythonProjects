#will convert lb to kg

while True:
    try:

        lb = float(input('Enter the number of pounds'))
        kg = lb * .45
        print(str(round(10, 2)) + ' lb equals ' + str(round(kg, 2)) + ' kg.')
        if kg >= 50:
            print('This is heavy')
        elif kg <= 10:
            print('This is light')
        else:
            print('This is correct')         
    except ValueError:
        continue
