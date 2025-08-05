students = []
books = ["Superman", "Ironman", "Batman"]
cities = ["Mumabi", "Pune", "Delhi"]
marks = [67, 92, 73, 81, 47]

# list methods
books.append("Antman")
books.insert(2, "Shaktiman")

# books.remove("Ironman")
index = 2
print(books[0: index])
print(books[index+1:])
nbooks = books[0: index]
nbooks.extend(books[index+1:])
print("Nbooks: ",nbooks)

# books.sort()
books.sort(reverse=True)

books.reverse()

# access
print(type(books))
print("All books",books)
print("First Book",books[0])
print("Last Book",books[len(books)-1])
print("Last Book",books[-1])


# Tuple - Un-changable, readable
countries = ("India", "USA", "Japan")


""" store 5 marks 
- find average
- find min
- find max
- sort in descending order
"""