import re 

print(type(re))

pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email = "_arunkumar@gmail.com"

print(re.match(pattern, email) is not None)