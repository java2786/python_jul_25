# 1. Tuple -  ordered collection - faster than list

my_tuple = (10, 20, 30)
print(my_tuple)
print("First:",my_tuple[0]) # Accessing
print("Last:",my_tuple[-1])
print("Last:",my_tuple[len(my_tuple)-1])
# my_tuple[0] = 40 # Error: Tuples are immutable
print(my_tuple)

# 2. Sets
my_set = {"Ramesh", "Suresh", "Dinesh", "Mahesh", "Suresh", "Dinesh", "Mahesh" }
# my_set['1'] = "January" # dictionary -> key pair
# my_set = {"1": "January", "2": "February"} # dictionary -> key pair
print(type(my_set))
print(my_set)
my_set.add("Hithes")
my_set.add("Rajesh")
my_set.add("Rajesh")
my_set.add("Mahesh")

my_set.remove("Rajesh")
print(my_set)

all_movies = {"spiderman", "hulk", "superman","hulk", "bahubali", "player", "KKKG", "ABC", "Andaz Apna Apna"}
ramesh_movies = {"spiderman", "hulk", "superman"}
mahesh_movies = {"hulk", "bahubali", "player"}

print(f"Full list: {ramesh_movies.union(mahesh_movies)}")
print(f"Common movie: {ramesh_movies.intersection(mahesh_movies)}")
print(f"not watched by mahesh: {all_movies.difference(mahesh_movies)}")

# 3. Dictionary -> key: value

# online shopping -> Cart => Dictionary

# key - value
# mobile - number, decimal, list, set, object, tuple
cart = {
    "mobile": ("mobile", 12000, 3),
    "shirt": {"item": "shirt", "price": 500, "quantity": 5},
    "book": {"item": "book", "price": 150, "quantity": 1},
}



# 4. List


# Ordered Collection - Practice 
""" 
1. Create a tuple with 5 student scores and print average of the scores
2. Create a list of 10 scores and remove duplicates from the list
3. Create a dictionary with 5 students with name and marks and print students who scored more than 70
"""