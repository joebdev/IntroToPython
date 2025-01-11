# 1. Concatenate two strings, one with your first name and one with your last, to create a new string with your full name
first_name = 'Joe'
last_name = 'Baney'
full_name = first_name + ' ' + last_name
print(full_name)

# 2. Use the REPL and the arithmetic operators to extract the individual digits of 4936
number = 4936
ones = number % 10
# print(ones)

number = number // 10
tens = number % 10
# print(tens)

number = number // 10
hundreds = number % 10
# print(hundreds)

thousands = number // 10
# print(thousands)

# 3. What does the following code do? Why?
print('5' + '10') # this would be '510', it concatenates the 5 to the 10 because they're both strings, not integers. 

# 4. Refactor the code from the previous exercise to use coercion to print 15 instead
print(int('5') + int('10'))

# 5. Will an error occur if you try to access a list limit with an index greater than or equal to the list's length? For example:
foo = ['a', 'b', 'c']
# print(foo[3]) # Yes, an error will occur, because the list doesn't have a value at index[3], it doesn't exist. 

# 6. To what value does the following expression evaluate?
'foo' == 'Foo' # It's false, because letter capitalization matters in comparisons. 

# 7. What will the following code do? Why?
int('3.1415') # Throws an error, because it would need to be of type float, instead of int. 

# 8. To what value does the following expression evaluate?
'12' < '9' # True, because the 9 is occurs further in the lexigraphical ordering than '1'.