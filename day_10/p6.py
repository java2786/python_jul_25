# palindrome - rev + compare

n = 67576
copy = n 
rev = 0

while n>0:
    ld = n%10
    rev = rev*10 + ld 
    n = n // 10 

if copy == rev:
    print(f"{copy} is palindrom")
else:
    print(f"{copy} is not plaindrom")