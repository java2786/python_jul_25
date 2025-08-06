""" store 5 marks 
- insert second marks as 68
- find average
- find min
- find max
- sort in descending order
"""

marks = [75, 98, 92, 67, 81]
print(marks)
# marks[1] = 68
marks.insert(1, 68)
print(marks)

count = len(marks) # 6
sum = 0
minVal = marks[0]

for i in range(count):
    sum = marks[i] + sum
    if minVal > marks[i]:
        minVal = marks[i]

        
    
average = sum / count 

print(average)
print(min(marks))
print(max(marks))
print(minVal)

# marks.sort()
# marks.reverse()

marks.sort(reverse=True)

print(marks)

# delete last
del marks[-1]
print(marks)