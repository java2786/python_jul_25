num = 82 # 64+4 => 68 => 36 + 64 => 100 -> 1

while num>9:
    sum = 0
    while num > 0:
        last = num % 10
        sum = sum + (last * last)
        num = num // 10
        
    if sum > 9:
        num = sum 
    else:
        if(sum == 1):
            print("Happy:",sum)
        else:
            print("Not Happy:",sum)
