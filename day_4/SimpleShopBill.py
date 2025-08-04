# Task 2: Simple Shop Bill
# Create a program that: 
# 1. Takes item name and price from user 
# 2. Calculates total with 18% GST 
# 3. Displays bill format

item_1 = input("Enter item name: ")
price_1 = int(input("Enter amount: "))
total = (price_1) * 1.18

item_2 = input("Enter item name: ")
price_2 = int(input("Enter amount: "))
totalbill = (price_1 + price_2) * 1.18


print(totalbill)