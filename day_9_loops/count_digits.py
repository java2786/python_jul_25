num = 32        # 32
count = 0       # 0

while num>0:
    num = num//10
    count = count + 1

print("Num",num)
print("Total digits are",count)