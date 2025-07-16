# Input two numbers and print which one is greater using only comparison operators.

a = input("Enter first num: ")
b = input("Enter second num: ")

print("A:",a)
print("B:",b)

x = int(a)
y = int(b)

print(type(a))
print(type(x))


# Method one to compare
'''
if(x>y):
    print(f"{x} is greater than {y}")
else:
    if(x<y):
        print(f"{y} is greater than {x}")
    else:
        print(f"Both values are {x}")
'''        
# Method two to compare
if(x>y):
    print(f"{x} is greater than {y}")
elif(x<y):
    print(f"{y} is greater than {x}")
else:
    print(f"Both values are {x}")
