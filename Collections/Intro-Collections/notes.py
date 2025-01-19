# Collection Types
# letters = ['a', 'b', 'c', 'd']
# print(letters[0]) # a
# print(letters[1]) # b


# Sets - unordered collection of unique object. 
    # Cannot be indexed
    # Cannot have duplicate values
    # Python has two types of sets: Regular sets and Frozen Sets
        # Sets are mutable
        # Frozen sets are immutable

letters = {'a', 'b', 'c'}
letters.add('d') # <-- adds 'd' to the letters set 
print(letters) 

frozen_letters = frozenset(letters)
# frozen_letters.add('e') # <-- would result in an error, frozensets can't be mutated

# sets may contain multiple different kinds of objects
my_set = {
    'May',
    2.99,
    (None, True, False),
    range(5)
}

# Python ignores any attempts to add duplicate entries to a set
new_letters = {'a', 'b', 'c', 'b', 'a'} # <-- this will still only contain a, b, c


# Mappings - maintain an unordered collection of key:value pairs. 
    # are accessed by their keys

# Dictionaries have the following characteristics
    # mutable
    # keys must be unique
    # keys must be "hashable" values
    # values in each k:v pair may be any object

d = {'a': 1, (1, 3): 3, 1: 'x'}
print(d)


# Sequence Constructors
# String Constructor
str() # returns ""
str('abc') # returns 'abc'
str(42) # returns '42'
str(3.141592) # returns '3.141592'
str(range(3, 7)) # returns 'range(3, 7)'

# Range Constructor
# range(start, stop, step)
r = range(5, 12, 2) # [5, 7, 9, 11]
r = range(12, 8, -1) # [12, 11, 10, 9]
r = range(12, 5, -2) # [12, 10, 8, 6]

# List, Tuple, Set, and Frozen Set Constructors
my_str = 'Python'
my_list = list(my_str)
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)

my_set = set(my_tuple)
print(my_set)