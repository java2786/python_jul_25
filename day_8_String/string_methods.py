fname = 'ramesh'
lname = 'MITTAL'

# Hello - Ramesh Mittal
print("Hello -",fname,lname) # Hello - ramesh MITTAL
print("Hello -",fname.upper(),lname.lower()) # Hello - RAMESH mittal

print("Capitalize: ",fname[0].upper(),fname[1:].lower(), sep="")
print("Capitalize:",lname.capitalize())

# output
# print("Hello -",fname.capitalize(),lname.capitalize())
output = "Hello - "+fname.capitalize()+" "+lname.capitalize()
print(output)

# replace Hello with Welcome
output = output.replace("Hello", "Welcome")
print(output)



# first char
# print("First char",fname[0])
# print("total chars",len(fname))
# print("Last char",fname[len(fname)-1])
# print("Last char",fname[-1])
# print("substring",fname[0: 3])



username = input("Enter your name: ")
print("Welcome", username.strip())


# Home work - Input email and verify if it is valid email address
# simple
# arunkumar@gmail.com 


# convert text into uppercase/lowercase/capitalize, part string

# I like python and python likes me.
# python -> find
