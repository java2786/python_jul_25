# Core Python table of contents 

| Chapter | Title               | Description                                                  |
|---------|---------------------|--------------------------------------------------------------|
| 1       | Syntax, Variables, Data Types | Introduction to Python syntax, variables, and data types.   |
| 2       | Control Structures  | Conditional statements and loops (if, for, while).           |
| 3       | Functions           | Defining and calling functions, parameters, and return values.|
| 4       | Data Structures     | Lists, tuples, sets, and dictionaries.                       |
| 5       | File Handling       | Reading from and writing to files.                           |
| 6       | Exception Handling  | Understanding exceptions and using try/except blocks.        |



# Chapter 1: Syntax, Variables, Data Types
```python
student_name = "Ramesh"
subject_marks = {"Math": 78, "Science": 85, "English": 69}  # Dictionary with subject marks
```

# Chapter 2: Control Structures
```python
total_marks = 0
for subject, marks in subject_marks.items():
    total_marks += marks

percentage = total_marks / len(subject_marks)

if percentage >= 75:
    grade = "Distinction"
elif percentage >= 60:
    grade = "First Class"
else:
    grade = "Second Class"
```

# Chapter 3: Functions
```python
def display_result(name, percentage, grade):
    print(f"Student: {name}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
```

# Chapter 4: Data Structures
```python
students_list = [student_name]
students_tuple = tuple(students_list)  # Tuple example
unique_subjects = set(subject_marks.keys())  # Set example
```

# Chapter 5: File Handling
```python
with open("student_result.txt", "a") as file:
    file.write(f"Name: {student_name}\n")
    file.write(f"Percentage: {percentage:.2f}%\n")
    file.write(f"Grade: {grade}\n")
```

# Chapter 6: Exception Handling
```python
try:
    with open("student_result.txt", "r") as file:
        print("\n--- Saved Result ---")
        print(file.read())
except FileNotFoundError:
    print("Result file not found.")
```

# Display final output
```python
display_result(student_name, percentage, grade)
```
