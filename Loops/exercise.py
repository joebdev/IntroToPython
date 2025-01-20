# 1. The following code causes an infinite loop. Why?
# counter = 0
# while counter < 5:
#     print(counter)

# It's because counters value is never changed from 0

# 2. Modify the age.py program you wrote in exercise 3 of Input/Output chapter. The updated code should use a for loop to display the future ages
    # Write a program named age.py that asks the user to enter their age, then calculates and reports the future age 10, 20, 30 and 40 years from now
# age = int(input("What is your current age? "))
# print(f'You are {age} years old.')

# for i in range(10, 50, 10):
#     print(f'In {i * 10} years, you will be {age + i}')

# 3. Use a while loop to print the numbers in my_list, one per line, then do the same with a for loop
my_list = [6, 3, 0, 11, 20, 4, 17]
index = 0

# while index < len(my_list):
#     print(my_list[index])
#     index += 1

# for number in my_list:
#     print(number)

# 4. Use a while loop to print all the numbers in my_list with even values, one per line, then print the odd numbers using a for loop
# while index < len(my_list):
#     if my_list[index] % 2 == 0:
#         print(my_list[index])
    
#     index += 1

# for number in my_list:
#     if number % 2 != 0:
#         print(number)

# 5. Print all of the even numbers in the following list of nested lists. Don't use any while loops.
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0]
]

for list in my_list:
    for number in list:
        if number % 2 == 0:
            print(number)

# 6. Let's try another variation on the even/odd-numbers theme.
# We'll return to the simpler one-dimensional version of my_list. 
    # In this problem, you should write code that creates a new list with one element for each number in my_list. If the original number is an even, 
    # then the corresponding element in the new list should contain the string 'even'; otherwise, the element should contain 'odd'.
my_list = [1, 3, 6, 11, 4, 2, 4, 9, 17, 16, 0]
word_list = []

for number in my_list:
    if number % 2 == 0:
        word_list.append('even')
    else:
        word_list.append('odd')

print(word_list)

# 7. Write a find_integers function that returns a list of all integers from my_tuple:
my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(tup):
    int_list = []
    for item in tup:
        if type(item) is int:
            int_list.append(item)
    return int_list

integers = find_integers(my_tuple)
# print(integers)                    # [1, 3, -4]

# 8. Write a comprehension that creates a dict object whose keys are strings and whose values are the length of the corresponding key. Only keys with odd lengths
    # should be used in the dict. Use the set given by my_set as the source of strings

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

cats = { name: len(name) for name in my_set if len(name) % 2 != 0}
print(cats)


# 9. Write a function that computes and returns the factorial of anumber by using a for or while loop. The factorial of a positive integer n, is defined as the product of all integers
    # between 1 and n, inclusive:

def factorial(n):
    current = 1
    for num in range(1, n + 1):
        current *= num
    
    return current

print(factorial(5))

# 10. The following code uses the randrange function from Python's random library to obtain and print a random integer within a given range. Using a while loop, it keeps running until it finds
    # a random number that matches the last number in the range. Refactor the code so it doesn't require two different invocations of randrange

import random

highest = 10
while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break

# 11. Print all the even numbers in the following list of nested lists. This time don't use any for loops.
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index = 0
while index < len(my_list):
    inner = 0
    while inner < len(my_list[index]):
        inner_item = my_list[index][inner]
        if inner_item % 2 == 0:
            print(inner_item)
        inner += 1
    index += 1