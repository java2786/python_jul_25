# 2, 5 -> 32
# 4, 3 -> 625


def power(num, power):
    result = 1
    for i in range(power):
        result = result * num
    return result

def sum(*nums):
    r = 0
    for num in nums:
        r = r + num 
    return r

print(power(2,3))
print(power(2,4))
print(power(3,3))
print(power(5,3))
print(power(2, 10))

print("========")
print(sum(3,5))
print(sum(3,5, 6))
print(sum(3))
print(sum(3,5,4,5,6,7,8))



