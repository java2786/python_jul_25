# Input an amount in INR and convert it to USD (assume fixed conversion rate).

amount = input("Enter some amount: ")
print(type(amount))

amount = int(amount)
print(type(amount))

# 83 * 1Rs -> $1
# 1Rs -> $?1/83 

# 10 * 1Rs -> $?1/83 * 10

# 1Rs = $0.012
print(f"{amount}Rs is equals to ${0.012*amount}")

