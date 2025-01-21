# 1. In your own words, explain the difference between these two expressions.
# my_object1 == my_object2 # <-- do they equal the same thing, so are they both looking at a variable that is 'cat'
# my_object1 is my_object2 # <-- are they the same thing, do they point to the same object in memory?

# 2. Without running this code, what will it print? Why?
set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2) # {42, 'Monty Python', ('a', 'b', 'c',), (5, 6, 7, 8, 9)}

# 3. Without running this code, what will print? Why?
dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python']) # The original ouput, dict2 is making a new dict from dict1

# 4. Without running this code, what will print? Why?
dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a']) # it's 42, dict() creates a shallow copy, so mutations can be seen in both dicts

# 5. Write some cody to create a deep copy of the dict1 object and assign it to the dict2. You should only modify the code where indicated.
# You may modify this line
import copy

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1) # You may modify the `???` part
            # of this line

# All of these should print False
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

# 6. The following program is nearly identical to that of the previous exercise. However, this time, it should create a shallow copy of dict1. 
    # You are not allowed to use the copy module in this exercise. 

dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1) # You may modify the `???` part
            # of this line

print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])