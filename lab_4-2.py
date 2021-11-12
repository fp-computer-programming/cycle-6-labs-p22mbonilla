# Author MB 11/12/2021

subjects = ['Math', 'Science', 'English']
print(subjects)

subjects.append('Spanish')
print(subjects)

print(subjects.index('English'))

subjects.sort()
print(subjects)

more_subjects = subjects.copy()

more_subjects.reverse()
print(more_subjects)
