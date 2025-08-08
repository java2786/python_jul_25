a = int(input("Enter first num: "))
b = int(input("Enter second num: "))
try:
    print(a/b)
    print("After divide")
except ZeroDivisionError:
    print("Cant divide by zero")
    
print("Bye Bye")