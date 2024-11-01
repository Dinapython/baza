grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2],
          [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
name_students = sorted(students)

average_score = []
for num in grades:
    value = sum(num)/len(num)
    average_score.append(value)

key_value = dict(zip(name_students, average_score))
print(key_value)