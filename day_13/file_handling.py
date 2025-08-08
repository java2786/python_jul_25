# file handling using python
# filepath = "/Volumes/My Shared Files/shared/thispc_host/python_9.30_jul_25/day_13/abc.txt"
# with open(filepath) as file_obj:
#     content = file_obj.read()
    
# print(content)


# write data into a file
filepath = "/Volumes/My Shared Files/shared/thispc_host/python_9.30_jul_25/day_13/abc.txt"
with open(filepath, 'a') as file_obj:
    file_obj.write("I am in India")
    file_obj.write("\n")