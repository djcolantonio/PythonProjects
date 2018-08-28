
def spam():          # create a function spam() that contains
    global eggs      # makes eggs a global variable
    eggs = 'Hello'   # eggs is a local variable, it has a value assigned Hello
    print(eggs)     # whatever the value of eggs will be printed

eggs = 100       # a gloabl variable eggs is created and 100 is assigned to it
spam()      # the function spam is called, whatever the value of eggs is printed
print(eggs) # the value assigned to the goabl eggs is printed
