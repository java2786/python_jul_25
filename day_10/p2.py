# print all the digits
# show sum of all the digits
n = 7752    
sum = 0
while n>0:
    ld = n%10           # 7    
    sum = sum + ld      # 21
    n = n // 10         #  0
    print("ld",ld,"n",n,"sum",sum)
    
# print("Sum",sum)
print("ByeBye")