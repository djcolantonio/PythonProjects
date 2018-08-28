def isZipCode (text):
    if len(text) !=12:
        return False
    for i in range (0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range (4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
            return False
    for i in range (8,12):
        if not text[i].isdecimal():
            return False
    return True

print(isZipCode(''))

message = 'My Zip codes are 12345, 06901, 12387, 10999, 67345'
for i in range (len(message)):
    zipcode = message[i:i+12]
    if isZipCode(zipcode):
        print('zipcode found: ' + zipcode)
        print('zipcode search is complete.')

        
        
