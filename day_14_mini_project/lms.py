import os 

BOOKS_FILE = "books.txt"
USERS_FILE = "users.txt"
def load_books():
    # print("File is available",os.path.exists(BOOKS_FILE))
    if(os.path.exists(BOOKS_FILE)):
        with open(BOOKS_FILE, 'r') as file: 
            # print("reading lines")
            lines = []
            for line in file:
                # print(line.strip())
                lines.append(line.strip())
                
            return lines  
    else:
        return []
    
def user_registeration():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    with open(USERS_FILE, 'a') as file: 
        file.write(f"{name},{email},{password},0\n")
    
def user_login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    found_user = None
    with open(USERS_FILE, 'r') as file:
        for line in file:
            user_list = line.strip().split(",")
            if email == user_list[1] and password == user_list[2]:
                print("valid user")
                found_user = (user_list[0], user_list[1], user_list[3])
                return found_user
            else:
                print("invalid user")
        return None

def main_menu():
    while True:
        print("***** Welcome to Library *****")     
        print("1. Open Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if(choice == "1"):
            print("Registration")
            user_registeration() 
        elif choice == "2":
            # print("Login")
            user = user_login() 
            print(user)
            if user == None:
                print("Login failed")
            else:
                print("Login successful")
        elif choice == "3":
            break 
        else:
            print("Invalid choice. Try again.")

# books = load_books()
# print(books)

# user_registeration()

# user = user_login()
# print("login: ", user)

main_menu()