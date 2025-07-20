# h_cm = int(input("Enter your height (cm): "))
# h_m = h_cm/100
# print(f"{h_cm}cm = {h_m}m")




# h_m = float(input("Enter your height (m): "))
# print(f"Your height is {h_m}meter")

# h_f = float(input("Enter your height (feet): "))
# print(f"Your height is {h_f}feet")





h_f = int(input("Enter your height (f): "))
h_i = int(input("Enter your height (i): "))
print(f"Your height is {h_f}feet and {h_i}inch")

h_m = (((h_f * 12)+h_i)*2.54)/100
print(f"Your height is {h_m:.2f}meter")



