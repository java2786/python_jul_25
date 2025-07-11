print("Hello user, How are you ?")
print("Today, we are here to learn python")

print("---------")

print("My name is Arun Kumar.\nI live in Delhi.\nI am 40 years old.\nI do train students on multiple languages.")

print("---------")

print("I am Arun Kumar.\
\nI live in Delhi.\
\nI am 40 years old.\
\nI do train students on multiple languages.")

print("----Variables-----")
name = "Mahesh"
age = 18
address = "Pune"
work = "study in abc college"

print(name)
print(age)
print(address)
print(work)

print("\n----\n")
print("I am",name,".\nI live in ",address,".\nI am ",age," years old.\nI do ",work,".")

print("\n----\n")
print("I am",name,".\nI live in ",address,".\nI am ",age," years old.\nI do ",work,".")
print(f"-->I am {name}.\nI live in {address}.\nI am {age} years old.\nI do {work}.")


# voting valid
if age >= 18:
    print(f"{name} is adult")
else:
    print(f"{name} is minor")