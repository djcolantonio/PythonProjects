def anyVar():
    global name
    name = 'eggs'
    print(name)

name = 22
anyVar()
print(name)
