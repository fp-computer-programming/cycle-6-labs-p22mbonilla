# Author MB 11/12/2021

color = ['red', 'blue', 'yellow', 'orange']
color.extend(['red', 'blue', 'yellow'])
print(color)

print(color.count('yellow'))

color.insert(3, 'purple')
print(color)

color.clear()
print(color)

print(color.count('red'))
