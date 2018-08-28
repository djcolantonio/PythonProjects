
# this converts F into C. C = (F-32)*5/9
F = int(input('Enter temp in Farenheit:' ))
C = (F-32) * 5/9
print( str(F) + ' in Celcius is ' + str('%.2F'%C))

# this converts C into F. F = 9.0/5.0 * C + 32
C = int(input('Enter temp in Celcius:' ))
F = (9.0/5.0) * (C + 32)
print( str(C) + ' in Farenheit is ' + str('%.2F'%F))



