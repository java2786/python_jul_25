students = [
    {'name': 'Ramesh', 'age': 23, 'subjects':{'math': 68, 'science': 81, 'english': 72}, 'contacts': [7634637638, 788873738]},
    {'name': 'Mahesh', 'age': 21, 'subjects':{'math': 71, 'science': 78, 'english': 67}, 'contacts': [4566778]}
]

# print(students)
# print(students[0])
# print(students[0]['subjects']['math'])

# students[1]['contacts'] = [4566778, 9222876, 988678]
students[1]['contacts'].append(988678)

students[1]['contacts'][1] = 8787878

print(students)