# 1.
def first(list):
    return list[0] if len(list) != 0 else None

print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))

# 2. 
def last(list):
    return list[-1] if len(list) != 0 else None

print(last(['Earth', 'Moon', 'Mars'])) # Mars
print(last([])) # None

# 3. 
energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
energy.remove('fossil')
energy.append('geothermal')
print(energy)

# 4. 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alpha_list = list(alphabet)
print(alpha_list)

# 5. 
scores = [96, 47, 113, 89, 100, 102]
count = 0
for score in scores:
    if score >= 100:
        count += 1

print(count)

# 6. 
vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

for list in vocabulary:
    for word in list:
        print(word)

# 7. 
# It should print True, because they both hold the same values in them
list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)

# 8. 
# some_value1 = [0, 1, 0, 0, 1]
# some_value2 = 'I leave you my Kingdon, take good care of it.'

# isinstance(some_value1, list)
# isinstance(some_value2, list)

# 9. 
destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(place, list):
    for item in list:
        if item == place:
            return True

    return False
        
print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False

# 10. 
passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']
str_pass = "-".join(passcode)
print(str_pass)

# 11. 
grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

while grocery_list:
    checked = grocery_list.pop(0)
    print(checked)

print(grocery_list)