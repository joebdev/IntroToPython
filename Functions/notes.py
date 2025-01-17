# Calling Functions
def hello():
    print('Hello')
    return True
# hello()
# print(hello())

# Built-in Functions
print(min(-10, 5, 12, -20)) # -20
print(max(-10, 5, 12, 0, -20)) # 12

# ord and chr
# ord gives the value of the character
print(ord('a')) # 97
print(ord('A')) # 65

#chr does the opposite of ord
print(chr(97)) # a
print(chr(65)) # A

# Any and All
# any returns true if any element in the collection is truth, false if they're all falsy. all returns true only if all elements are truthy, otherwise, false. 
collection1 = [False, False, False]
collection2 = (False, True, False)
collection3 = {True, True, True}

print(any(collection1)) # False
print(any(collection2)) # True
print(all(collection1)) # False
print(all(collection2)) # False
print(all(collection3)) # True

# Example:
numbers = [2, 5, 8, 10, 13]
print(any([number % 2 == 0 for number in numbers])) # True <-- some numbers are even
print(all([number % 2 == 0 for number in numbers])) # False <-- not all numbers are even


# Creating Functions
# def say():
#     """
#     The say function prints "Hi!" <-- Triple quotes allows programmers to add notes on what the function will do -- NOT used at Launch School
#     """
#     print("Output from say!")

# print(say.__doc__) # <-- prints out the """ notes from the say function
# say()


# Scope
def well_howdy(who):
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Angie')
# print(greeting) # Remember, this isn't global scope, since it was defined in the function, it's only got local scope


# Arguments and Parameters
# def say(text):
#     print('--> ' + text)

# say('Hello')
# say('hi')


# Return Values
def add(a, b):
    return a + b # Python does not allow for implicit returns, you must use the return keyword, even if the function is only one line of code
print(add(2, 3))

# This function is a predicate, a function that always returns a bool value, true or false. 
def is_digit(char):
    if char >= '0' and char <= '9':
        return True
    
    return False


# Default Parameters
def say(text='hello'): # you can choose which parameter gets default values, say(a, b, c='text', d) <-- like this, BUT ALL subsequent parameters MUST have default values, so D would also need one. 
    print(text + '!')

say('Howdy')
say()


# Functions vs. Methods
my_str = 'abc-123-def'
print(my_str.upper()) # <-- .upper() is your method


# Mutating the Caller
odd_numbers = [1, 3, 5, 7, 9]
odd_numbers.pop() # <-- removes 9, mutating odd_numbers

def add_new_numbers(my_list):
    my_list.append(9)

numbers = [1, 2, 3, 4, 5]
add_new_numbers(numbers) # <-- would add 9 to the numbers list, making this function mutate the original numbers list, because it mutates it's argument. This should be avoided, as it can be hard to debug

