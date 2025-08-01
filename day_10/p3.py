# count even and odd digits
n = 43628
evens = 0
odds = 0

while n>0:
    ld = n % 10
    if ld%2==0:
        # print(ld,"is even number")
        evens = evens+1
    else:
        # print(ld,"is odd number")
        odds = odds + 1
        
    n = n // 10
    
    
print("Evens",evens,"Odds:",odds)