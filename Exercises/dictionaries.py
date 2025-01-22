# 1. 
car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80000
}

# 2. 
car['year'] = 2003

# 3. 
del car['mileage']

# 4. 
print(car['color'])

# 5. 
print(len(car))

# 6. 
student = {
    'id': 123,
    'grade': 'B',
}
print('name' in student)
print('grade' in student)

# 7. 
vehicles = {
    'car': {
        'type': 'sedan',
        'color': 'blue',
        'year': 2003
    },

    'truck': {
        'type': 'pickup',
        'color': 'red',
        'year': 1998
    }
}

# 8. 
car = [
    ['type', 'sedan'],
    ['color', 'blue'],
    ['mileage', 80000]
]

# 9. 
numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_numbers = []

for value in numbers.values():
    half_numbers.append(value // 2)

print(half_numbers)

# 10. 
numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for key, value in numbers.items():
    print(f'A {key} number is {value}')