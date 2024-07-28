# Initialize sequences
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
avg_grades = []

# Convert unordered set to sorted ordered list

student_l = list(students)
print(student_l)
student_l.sort()  #sorted(list(students))
print('Sorted list of students:', student_l)

# Calculate AVG grades and put them into list
for grade in grades: avg_grades.append(sum(grade)/len(grade))
print('List of average grades:', avg_grades)

# Pack two lists into dictionary
grades_registry = tuple(zip(student_l, avg_grades))
print("Students' average grades:", grades_registry)
grades_registry = dict(zip(student_l, avg_grades))
print("Students' average grades:", grades_registry)
