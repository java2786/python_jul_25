# print all strong numbers from 1 to 10000
for n in range(1,100001):
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
