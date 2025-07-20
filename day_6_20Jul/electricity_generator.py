# Electricity Bill Calculation
#     For the first 100 units: 1.5 per unit
#     For the next 100 units: 2.5 per unit
#     Beyond 200 units: 3.5 per unit
# Example:
#     Input: Units = 250 => 100 + 100 + 50
#     Output: Bill = 575
# Example:
#     Input: Units = 120 => 150 + 50
#     Output: Bill = 200

# units = int(input("Enter consumed units: "))
# bill = 0
# if(units>200):
#     bill = bill + (units - 200)*3.5
#     units = 200

# if(units>100):
#     bill = bill + (units - 100)*2.5
#     units = 100

# bill = bill + (units)*1.5

# print("Final bill: ",bill)


def calculate_electricity_bill(units):
    bill = 0
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = (100 * 1.5) + ((units - 100) * 2.5)
    else:
        bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 3.5)
    return bill 

units = 250
bill = calculate_electricity_bill(units)
print(f"Units = {units}")
print(f"Bill = {bill}")