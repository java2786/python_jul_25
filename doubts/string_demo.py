name = "sUpeRmAN"

print(name)
print("Upper:",name.upper())
print("Lower:",name.lower())
print("Capitalize:",name.capitalize())

print("Find man 1",name.__contains__("man"))
print("Find man 2",name.lower().__contains__("man"))
print("Find MAN 3",name.__contains__("MAN"))
print("Find MAN 4",name.upper().__contains__("MAN"))
print("Index", name.lower().index("m"))
print("Find", name.lower().find("man"))

print("Substring",name.lower()[5:])


print("\n\n===========\n\n")
print("Find man in",name,"=>",name.__contains__("man"))
lname = name.lower()
print(type(lname))
print("Find man in",lname,"=>",lname.__contains__("man"))
print("Find man in",lname,"=>",name.lower().__contains__("man"))


