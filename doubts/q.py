amount = "125d"

# amount[0:len(amount)-1]
amount = int(amount[0:-1])
print(amount)
print(type(amount))

inr = 86.47*amount
print(inr,"₹",sep="")

