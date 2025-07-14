n = input("Enter a number: ")

print(type(n))
print(type(int(n)))

# assignment operator
m = int(n)
print(f"/: {m/2}")
print(f"//: {m//2}")
print(f"%: {m%2}")

print("\n\n")

# == equality
print(f"Is {m} an even number: {m%2==0}")


# true => True
# True, False, None
# Is 31 an even number: Yes/No

if m%2==0:
    print(f"{m} is an even number.")
    print(f"{m} is not an odd number.")
else:
    print(f"{m} is not an even number.")
    print(f"{m} is an odd number.")

