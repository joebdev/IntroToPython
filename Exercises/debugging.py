# 1. 
# It was only supposed to recieve one argument, but was given 6 <-- they need to be in a list, the second one won't work, beacause it's just an int
def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among([0, 0, 1, 0, 2, 0])
# find_first_nonzero_among(1)

# 2. 
# Because true and false are strings, so since it's not an empty string, it will always be True
import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()

# 3. 
# The input needed to be coerced to take an int instead of a string
def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input())

print(f"The result is {multiply_by_five(number)}!")

# 4. 
# The code currently would replace the value of dog with the bowser, but since it's an list of names, we can just use append to add it. 
pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'].append('Bowser')

print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}

# 5. 
# It wasn't returning anything
def get_quote(person):
    if person == 'Yoda':
       return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
       return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
       return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print(''+ get_quote('Confucius') + '')

# 6. 
# range starts at 0 and goes to one before the ending number, so change it to be 1, 6
numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)

# 7. 
info = {'name': 'Srdjan', 'age': 38}

print(info.get('city', 'Unknown'))

# 8.
import copy
sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    new_list = copy.deepcopy(sub_list)
    matrix.append(new_list)

matrix[0][0] = "X"
matrix[0][1] = "O"
matrix[1][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]

# 9. 
# max_number being set to 0, meant that 0 was higher than all values in the third list, so to fix it, just set max_number to an item in the list
def find_maximum(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2

# 10. 
# Since product was set to 0, it was always going to be 0, since anything * 0 is 0, so setting product to 1, fixes it
def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0