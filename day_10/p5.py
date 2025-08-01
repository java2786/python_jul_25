# reverse the number -> 2634

n = 12345
r = 0
# s = (str)(n)
# print(s[::-1])

while n>0:
    ld = n%10
    n = n // 10
    r = r * 10 + ld 

print(r)