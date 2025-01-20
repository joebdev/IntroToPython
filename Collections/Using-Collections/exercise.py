# 1. Write Python code to print the seventh number of range(0, 25, 3)
my_range = range(0, 25, 3)
print(my_range[6])

# 2. Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c
school = 'Launch School'
print(school[4:10])

# 3. Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order from the original. It should exclude the first and last members of
    # the original. The result should be the tuple (4, 3, 2)

my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list.reverse()
new_tuple = my_list[1:4]
print(new_tuple)

# 4. This is a 3-part question. Consider the following dictionary:
    # Part 1: Write some code to print Bark by accessing the element associated with the key Dog
    # Part 2: Write some code to print None when you try to print the value associated with the non-existent key, Lizard
    # Part 3: Write some code to print Silence when you try to print the value associated with the non-existent key, Lizard

pets = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Bird': 'Tweet'
}

# Part 1
print(pets['Dog'])

# Part 2
print(pets.get('Lizard'))

# Part 3
print(pets.get('Lizard', '<silence>'))

# 5. Which of the following values can't be used as a key in a dict object, and why?
    # 'cat' # <-- can be
    # (3, 1, 4, 1, 5, 9, 2)
    # ['a', 'b'] # <-- can't be, because its mutable
    # {'a': 1, 'b': 2} # <-- can't be, it's mutable
    # range(5)
    # {1, 4, 9, 16, 25} # <-- can't be, it's mutable
    # 3
    # 0.0 
    # frozenset({1, 4, 9, 16, 25})

# 6. What will the following code print?
    # print('abc-def'.isalpha()) # False
    # print('abc_def'.isalpha()) # False
    # print('abc def'.isalpha()) # False
    # print('abc def'.isalpha() and # False
    #       'abc def'.isspace())
    # print('abc def'.isalpha() or # False
    #       'abc def'.isspace())
    # print('abcdef'.isalpha()) # True
    # print('31415'.isdigit()) # True
    # print('-31415'.isdigit()) # False
    # print('31_415'.isdigit()) # False
    # print('3.1415'.isdigit()) # False
    # print(''.isspace()) # False

# 7. Write Python code to replace all the : characters in the string below with +
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
print(info.replace(':', '+'))

# 8. Explain why the code below prints different values on lines 3 and 4.
text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8 <-- this one is slicing the string first, and then looking for the letter 'f'
print(text.rfind('f', 21, 35))    # 29 <-- this one is doing the rfind and looking for the 'f' in the current string

# 9. Write some code to replace the value 6 in the following nested list with 606:
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]
stuff[1][3] = 606
print(stuff)

# 10. Consider the following nested collection:
    # Write one line of code to print the activities Cocoa enjoys
cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])

# 11. Without running the following code, determine what each line should print.
    # print('johnson' in 'Joe Johnson') # False
    # print('sen' not in 'Joe Johnson') # True
    # print('Joe J' in 'Joe Johnson') # True
    # print(5 in range(5)) # False
    # print(5 in range(6)) # True
    # print(5 not in range(5, 10)) # False
    # print(0 in range(10, 0, -1)) # False
    # print(4 in {6, 5, 4, 3, 2, 1}) # True
    # print({1, 2, 3} in {1, 2, 3}) # False
    # print({3, 2} in {1, frozenset({2, 3})}) # True

# 12. Write some code that determines and prints wheter the number 3 appears inside each of these lists:
numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)

# 13. Without running the following code, determine what each print statement should print.
cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats) # True
print('Butter' in cats) # False <-- must match exactly
print('Butter' in cats[3]) # True
print('cheddar' in cats) # False

# 14. Assume you have the following sequences:
    # Write some code that combines the sequences into a list of tuples. Each should contain one member of each sequence. 
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

my_zipper = zip(my_str, my_list, my_tuple, my_range)
print(list(my_zipper))

# 15. Without running the following code, what values will be printed by line 10?
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys) # 'Cat', 'Bird', 'Snake'

