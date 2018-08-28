# this program will count the number of characters in the text

import pprint

message = 'Today we cover the dictionary data type. On thursday we will have the exam review'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
