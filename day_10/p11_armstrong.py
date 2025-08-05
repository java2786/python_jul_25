# num = 153 # 1^3 + 5^3 + 3^3
# num = 8 # 8^1 = 8
num = 1634 # 1^4 + 6^4 + 3^4 + 4^4 = 1+1296+81+256 = 1634
copy = num
result = 0

while num>0:
    m = num%10
    i = m*m*m
    result = result + i

    num = num//10

if copy == result:
    print(copy, "is an Armstrong Number")
else:
    print(copy, "is not Armstrong Number")
