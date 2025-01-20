# Indexing
seq = ('a', 'b', 'c')
seq[0] # 'a'
seq[1] # 'b'

# accessing the last element in a sequence
last_index = len(seq) - 1
# seq([last_index]) # 'c'
# seq[-1] # this also works


# Slicing
seq = 'abcdefghi'
print(seq[3:7]) # defg
print(seq[-6:-2]) # defg
print(seq[2:8:2]) # ceg, prints from [2] to [8] at a step of 2
print(seq[::-1]) # prints the sequence backwards


# Key-Based Access
my_dict = {
    'a': 'abc',
    37: 'def',
    (5, 6, 7): 'ghi',
    frozenset([1, 2]): 'jkl',
}

print(my_dict['a']) # 'abc'
print(my_dict[37]) # 'def
print(my_dict[(5, 6, 7)]) # ghi
print(my_dict[frozenset([1, 2])]) # jkl
 # if you're unsure if the key exists, use dict.get which will return none if that key doesn't exist
print(my_dict.get('nothing', 100)) # will return 100, it looks for the key nothing, which doesn't exist, so it takes the value given

# Dictionary keys must be immuatable, so you can't use lists. 

# Collection Membership
seq = [4, 'abcdef', (True, False, None)]
4 in seq # True
4 not in seq # False
'abcdef' in seq # True
'cde' in seq[1] # True
'acde' in seq[1] # False, they must be in the same order that they are in the seq. 

# Minimum and Maximum Members
my_set1 = {1, 4, -9, 16, 25, -36, -63, -1}
my_set2 = {'1', '4', '-9', '16', '25', '-36', '-1'}
print(min(my_set1), max(my_set1)) # -63 25
print(min(my_set2), max(my_set2)) # -1 4

# Cannot use min or max with heterogenous collections, so collections that have items with more than one type, like strings and ints

# Summation - returns the sum of all the collections numbers
numbers = (1, 1, 2, 3, 5, 8, 13, 21, 34)
sum(numbers) # 88 <-- only works with ints, use str.join for strings. 

# Locating Indices and Counting
names = ['Karl', 'Grace', 'Clare', 'Victor', 'Antonina', 'Allison', 'Trevor']
names.index('Clare') # 2 (The index in which Clare is located)
# names.index('Chris') # ValueError: 'Chris' is not in the list

numbers.count(1) # 2 (It appears in the collection twice)
numbers.count(3) # 1 (It only appears once)

# Index also works with strings
name = 'Karl Grace Clare Victor Antonina Trevor'
name.index('Clare') # 11
name.index('Trevor') # 33

# Merging Collections
iterable1 = [1, 2, 3]
iterable2 = ('Kim', 'Leslie', 'Bertie')
iterable3 = [None, True, False]

zipped_iterables = zip(iterable1, iterable2, iterable3)
print(list(zipped_iterables)) # change it to a list, and print it
# [
    #(1, 'Kim', None),
    #(2, 'Leslie', True),
    #(3, 'Bertie', False)
#]

# Zip is an *iterator*, it can only be consumed once, so if you try to iterate it more than one time, it will fail and return an empty []

# Operations in Dictionaries
people_phones = {
    'Chris': '111-2222',
    'Pete': '333-4444',
    'Clare': '555-6666'
}

print(people_phones.keys()) # dict_keys(['Chris', 'Pete', 'Clare'])
print(people_phones.values()) # dict_values(['111-2222', '333-4444', '555-6666'])
print(people_phones.items()) # returns the entire k:v pair

keys = people_phones.keys() # this and values will update autmatically as the changes below happen
values = people_phones.values()

print(keys)
print(values)

people_phones['Max'] = '123-4567' # adds max to the dictionary
people_phones['Pete'] = '345-6789' # updates Petes phone number
del people_phones['Chris'] # deletes chris


# Adding Elements to Mutable Sequences
numbers = [1, 2]
numbers.append(10) # numbers is now [1, 2, 10]

# seq.insert allows adding at a specific index
numbers.insert(0, 8) # so adds 8 before [0] giving you, [8, 1, 2]
numbers.insert(2, 6) # [8, 1, 6, 2]
numbers.insert(100, 55) # will add 55 at the end, since [100] doesn't exist
numbers.insert(-3, 33) # insert 33 before the 3rd element from the end [8, 1, 33, 6, 2, 55]

# seq.extend appends the contents of an iterable sequence to the calling sequence
numbers = [1, 2]
numbers.extend([7, 8]) # numbers is now [1, 2, 7, 8]

# Removing Elements from Mutable Sequences
# seq.remove searches for a specific object and removes the first occurence, if it doesn't exist, throws an error
my_list = [2, 4, 6, 8, 10]
my_list.remove(8) # [2, 4, 6, 10]

# seq.pop removes and returns an indexed element, if no index is given, it removes the last element
my_list.pop(1) # 4
my_list.pop() # 10

# seq.clear removes all elements
my_list.clear() # []

# Sorting Collections
names = ('Grace', 'Clare', 'Allison', 'Trevor')
print(sorted(names)) # they are now in abc order
print(names) # normal order, the previous line did NOT mutate
names = list(names) # changing it to a list
names.sort() # none, but names are now sorted, and the list IS mutated

# Reverse sort
sorted(names, reverse=True) # non mutating
names.sort(reverse=True) # mutating

words = ['abc', 'DEF', 'xyz', '123']
sorted(words) # 123, DEF, abc, xyz
sorted(words, key=str.casefold) # 123, abc, def, xyz <-- so it allows it to ignore casing and print them in abc order still

numbers = ['1', '5', '100', '15', '534', '53']
numbers.sort() # 1, 100, 15, 5, 53, 534 <-- strings, so it's printing from lowest first value to highest
numbers.sort(key=int) # 1, 5, 15, 53, 100, 534

# Reversing Sequences and Dictionaries
names = ('Grace', 'Clare', 'Allison', 'Trevor')
reversed_names = reversed(names) # This reverses them, but its a lazy sort, so you must change it to a tuple or list to view them
tuple(reversed(names)) # now the names are reversed

names = list(names)
names.reverse # None, but they are mutated and in reverse order now

my_dict = {'abc': 1, 'xyz': 23, 'pqr': 0, 'jkl': 5}
reversed_dict = reversed(my_dict) # same thing, turn it into a list first
list(reversed_dict) # the keys are now in reverse order

# String Operations
print("what's up?".capitalize()) # capitalizes first letter of the string
print('456ABC'.capitalize()) # converts remaining characters to lowercase

print("four SCORE and sEvEn".title()) # .title lowercases everything and capitalizes the first letter of each word
# punctation can lead to unexpected results
print("i can't believe it's already mid-july.".title()) # I can'T Believe It'S Already Mid-July.

# to only break at whitespace instead of punctuation as well, use capwords
import string
string.capwords("i can't believe it's already mid-july.") # now it prints properly

# swapcase swaps the casing of each letter
print("What's up?".swapcase()) # wHAT'S UP?
 
# Character Classification
'Hello'.isalpha() # True <-- isalpha checks to see if every character in the string is alphabetic
'Good-Bye'.isalpha() # False '-' is not a letter
'Four Score'.isalpha() # False: Space is not a letter

'12340'.isdigit() # True
'123.4'.isdigit() # False

# Stripping Characters
# .strip removes all whitespace before and after the string
# text = input(prompt).strip() # would remove all whitespace from the prompt input

text = 'aaabaacccabxyzabccba'
print(repr(text.strip('a'))) # removes the first a in text
print(text.strip('abc')) # 'xyz', removes everything except for the xyz

# lstrip removes all left leading characters and rstrip removes the right leading characters

# startswith and endswith
'Four score and seven'.startswith('Four score') # true
print('abc def'.startswith(('abc', 'xyz', 'stu'))) # True, can be used with a tuple of strings, so now it sees if it startswith any characters in that tuple

# Splitting and Joining Strings
text = ' Four   score and  seven years ago.   '
print(text.split()) # [Four, score, and, seven, years, ago.]
# you can tell python what to split on, instead of spaces
text = ',Four,score,and,,,seven,years,ago,'
text.split(',') # ['', 'Four', score, and, '', '', seven, years, ago, '']

# cannot split python strings into a list, you must use the list or tuple function instead
text = 'abcde'
list(text)
tuple(text)

words = ['You', 'were', 'lucky']
''.join(words) # Youwerelucky
' '.join(words) # You were lucky
','.join(words) # You,were,lucky

# Finding Substrings
school = 'launch school'
school.find(' ') # 6
school.find('l') # 0
school.find('h') # 5
school.find('hoo') # 9
school.find('x') # -1 <-- doesn't exist

# .rfind does the same thing, except in reverse order
school.rfind(' ') # 6
school.rfind('l') # 12
school.rfind('h') # 9

# Can also search slices by adding start and end arguments
text = 'abc abc def abc'
text.find(' ', 4) # 7 <-- start at index 4, and find the first space, which occurs at index 7
