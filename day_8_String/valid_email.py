# email = input("Enter you email address: ")
email = "arun_kumar@.gmail.com"

# email = "arun.kumar@.gmailcom"

"""
@ is available or not 
@ should occure only once
does not start with @
- should contain chars before @
does not end with @
- should contain domain after @
domain should contain char .
"""

# print('@' not in email) # not
# print('.' not in email) # not
# print(email.count('@') > 1) # more than 1
# print(email.startswith("@")) # starts with @
# print(email.endswith("@")) # ends with @
# print(email.startswith(".")) # starts with .
# print(email.endswith(".")) # ends with .



if '@' not in email:
    print("invalid email because @ is not available")
elif '.' not in email:
    print("invalid email because . is not available")
elif email.count('@') > 1:
    print("invalid email")
elif email.startswith("@"):
    print("invalid email")
elif email.endswith("@"):
    print("invalid email")
elif email.startswith("."):
    print("invalid email")
elif email.endswith("."):
    print("invalid email")
else:
    # domain should be after @
    indexOfAt = email.index("@")
    # indexOfDot = email.index(".", indexOfAt) # exception -> try catch
    # domain = email[(1+indexOfAt):]
    # print("Domain:",domain)
    # if '.' not in domain :
    #     print("invalid email as domain does not contain .")
    # elif domain.startswith("."):
    #     print("invalid, domain starts with .")
    # else:
    #     print(email,"is valid")
    
    domain = email[indexOfAt:]
    print("Domain:",domain)
    if '.' not in domain :
        print("invalid email as domain does not contain .")
    elif domain.index(".")<2:
        print("invalid, . occurs after @")
    else:
        print(email,"is valid")


# email = "arun.kumar@.gmail.com" -> invalid -> logic