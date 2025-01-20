# While Loops
# counter = 1
# while counter <= 20:
#     print(counter)
#     counter += 2

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0

# while index < len(names):
#     upper_name = names[index].upper()
#     upper_names.append(upper_name)
#     index += 1

# print(upper_names)

# For Loops
for name in names:
    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names)

# Looping through a string
for char in 'Launch School':
    print(char)

# Looping through a set
my_set = {1000, 2000, 3000, 4000, 5000}
for member in my_set:
    print(member)

# Looping through a dict
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)

# If you want to get the values instead:
for value in my_dict.values():
    print(value)

# To get K:V
for item in my_dict.items():
    print(item)

# A better way is to use tuple unpacking:
for (key, value) in my_dict.items():
    print(f'{key} = {value}')

# Nested Loops
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = []
for suit in suits:
    for rank in ranks:
        card = f'{rank} of {suit}'
        deck.append(card)

# print(deck)

# Controllling Loops
names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
for name in names:
    if name == 'Max':
        continue

    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names)

# Breaking out of a Loop
numbers = [3, 1, 5, 9, 2, 6, 4, 7]
found_item = -1
index = 0

while index < len(numbers):
    if numbers[index] == 5:
        found_item = index
        break
    
    index += 1

print(found_item)


# Do/While Loops
# keep_going = True
# while keep_going:
#     # main loop code is here

#     answer = input('Play again? (y/n) ')
#     if answer == 'n':
#         keep_going = False

# Simultaneous Iteration
forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

index = 0
while index < len(forenames):
    if index >= len(surnames):
        break

    forename = forenames[index]
    surname = surnames[index]
    print(f'{forename} {surname}')

    index += 1

# An easier method is to use zip
zipped_names = zip(forenames, surnames)
for forename, surname in zipped_names:
    print(f'{forename} {surname}')

# List Comprehension
squares = [number * number for number in range(5)]
print(squares)

multiples_of_6 = [ number for number in range(20) if number % 6 == 0]
print(multiples_of_6)

even_squares = [ number * number for number in range(10) if number % 2 == 0]
print(even_squares)

cats_colors = {
    'Tess': 'brown',
    'Leo': 'orange',
    'Fluffy': 'white',
    'Ben': 'black',
    'Kat': 'orange'
}

names = [name.upper() for name in cats_colors]
print(names)

names = [name.upper() for name in cats_colors if cats_colors[name] == 'orange' and name[0] == 'L']
print(names)

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10',
    'Jack', 'Queen', 'King', 'Ace',
]

deck = [ f'{rank} of {suit}'
         for suit in suits
         for rank in ranks ]

# print(deck)

# Dictionary Comprehensions
squares = { f'{number}-squared': number * number for number in range(1, 6)}
print(squares)

# Set Comprehensions
squares = { number * number for number in range(1, 6)}
print(squares)