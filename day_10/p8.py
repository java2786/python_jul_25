# Peterson number / Strong number
# digits factorial + sum => compare

# 153 => 1! + 5! + 3! = 1 + 120 + 6 = 127
# 145 => 1 + 24 + 120 = 145


n = 145
copy = n 
result = 0

while n>0:    
    m = n%10
    fact = 1
    # 4 * 3 * 2 * 1
    while m>0:
        # logic
        fact = fact * m 
        m = m-1 
    
    
    result = result + fact 
    n = n // 10 

if copy == result:
    print(f"{copy} is strong number")
else:
    print(f"{copy} is not strong number")

