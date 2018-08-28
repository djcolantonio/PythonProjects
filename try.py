def any_var(divided):
    try:
        return 100 / divided
    except: ZeroDivisionError:
            print('Error: Division by zero is not allowed.')

print(any_var(2))
print(any_var(5))
print(any_var(0))
print(any_var(10))
print(any_var(20))
    
