# Arithmetic Operations

# Addition
print(38 + 4) # 42
print(38.4 + 41.9) # 80.3

# Mixing Ints and floats
print(38 + 41.5) # 79.5

# Subtraction
print(38 - 4) # 34
print(38.4 - 41.9) # -3.5

# Mixing ints and floats
print(38 - 41.5) # -3.5

# Multiplication
print(38 * 4) # 152
print(38.4 * 41.1) # 1578.24

# Mixing Ints and Floats
print(38 * 41.5) # 1577.0

# Division with /
print(16 / 4) # 4.0
print(16 / 2.5) # 6.4
# When you divide to ints, two floats, or one of each with / the result is always a float

# Division with //
print(16 // 3) # 5
print(16 // -3) # -6
print(16 // 2.3) # 6.0
print(-16 // 2.3) # -7.0
# The // operator returns the largest whole number less than or equal to the floating point result. It rounds down to the nearest whole number

# Exponents **
print(16**3) # 4096 <-- Don't use spaces in exponents, this is equal to 16 * 16 * 16

# Modulo
print(15 % 3) # 0
print(16 % 3) # 1
print(17 % 3) # 2
print(18 % 3) # 0


# Floating Point Imprecision
print(0.1 + 0.2 == 0.3) # False
# This can cause serious problems in some applications, especially finance. One way around it is to use the math.isclose function (Happens because of the way real numbers are stored on computers)
import math
print(math.isclose(0.1 + 0.2, 0.3)) # True

# You can also use the decimal.Decimal type to make precise computations
from decimal import Decimal
Decimal('0.1') + Decimal('0.2') == Decimal('0.3') # True <- Always use strings with decimal.Decimal, if you use floats, you will lose the precise computation benefits


# Equality Comparisons
print(42 == 42) # True
print(42 == 43) # False
print('foo' == 'foo') # True
print('FOO' == 'foo') # False

# Inequality
print(42 != 42) # False
print(42 != 43) # True
print('foo' != 'foo') # False
print('FOO' != 'foo') # True


# Ordered Comparisons
print(42 < 41) # False
print(42 < 42) # False
print(42 <= 42) # True
print(42 < 43) # True

print('3' < '24') # False
print('24' < '3') # True

# String Concatenation
print('foo' + 'bar') # 'foobar'
print('1' + '2') # '12'
print('abc' * 3) # 'abcabcabc'


# Coercion
print(int('5')) # 5
print(float('3.141592')) # 3.141592

# Numbers to strings
print(str(5)) # '5'
print(str(3.141592)) # '3.141592'


# Implicit Coercion
# Python doing the coercion behind scenes. Like when adding 3 + 3.0, python will automatically do the coercion to give you 6.0 as a float.


# Determining Types
print(type(1)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type(True)) # <class 'bool'>
print(type('abc')) # <class 'str'>
print(type([1, 2, 3])) # <class 'list'>
print(type(None)) # <class 'NoneType'>

# Type with is operator
print(type('abc') is str) # True
print(type('abc') is int) # False

# String Representations <-- work at a lower level than str(), so it can some times return different values. 
my_str = 'abc'
print(my_str) # abc
print(str(my_str)) # abc
print(repr(my_str)) # 'abc' (note the quotes)


# Collection and String Lengths
print(len('Launch School')) # 13
print(len(range(5, 15))) # 10
print(len(range(5, 15, 3))) # 4
print(len(['a', 'b', 'c'])) # 3

# Indexing and Key Access
print(my_str[0]) # 'a'
print(my_str[1]) # 'b'

my_range = range(5, 8)
print(my_range[0]) # 5
print(my_range[1]) # 6

# my_dict = {'a': 1, 'b': 2, 'c':3}
# print(my_dict['a']) # 1
# print(my_dict['b']) # 2


# Using [] to update elements <-- Only used on Lists and Dictionaries
my_list = [1, 2, 3, 4]
my_list[2] = 6
print(my_list) # [1, 2, 6, 4]

my_dict = {
    'dog': 'barks',
    'cat': 'meows',
    'pig': 'oinks'
}

my_dict['pig'] = 'snorts' # changes 'oinks' to 'snorts'

my_dict['fish'] = 'glub glub' # adds a new key:value to my_dict with 'fish': 'glub glub'

