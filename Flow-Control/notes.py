# Conditionals

# value = int(input("Enter a number: "))
# if value == 3:
#     print("value is 3")
# else:
#     if value == 4:
#         print("value is 4")
#     else:
#         print("value is NOT 3 or 4")

# Rewriting the code above using an elif statement
value = int(input("Enter a number: "))
if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
else:
    print('value is NOT 3 or 4')

# Sometimes we leave an elif blank, and just put pass inside of the statement, which makes it do nothing, but if we do that, we should leave a comment to let others know why it's there


# Comparisons
print(5 == 5) # True
print(5 == 4) # False
print('abc' == 'abc') # True
print('abc' == 'abcd') # False
print(5 == '5') # False
print(5 == float(5)) # True

print('abc' == 'aBc') # False
print('abc'.lower() == 'aBc'.lower()) # True


# Inequality Operator
print(5 != 5) # False
print(5 != 4) # True


# Less than Operator
print(4 < 5) # True
print(5 < 4) # False

# Greater than Operator
print(4 > 5) # False
print(5 > 4) # True


# Logical Operators
print(not True) # False
print(not False) # True
print(not(4 == 4)) # False
print(not(4 != 4)) # True

# and || or operators
print((4 == 4) and (7 == 7)) # True
print((4 == 4) and (7 == 3)) # False

print((4 == 4) or (7 == 7)) # True
print((4 == 4) or (7 == 3)) # True

# Truthy and Falsy values
value = 5
if value:
    print(f'{value} is truthy')
else:
    print(f'{value} is falsy')


# Match/Case Statements
value = 7
match value:
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _: # Default case in Python
        print('value is neither 5 nor 6')

# To check multiple values you can use |
match value:
    case 1 | 2 | 3 | 4:
        print('value is less than 5')
    case 5 | 6:
        print('value is 5 or 6')
    case _:
        print('value is not 1, 2, 3, 4, 5, or 6')


# Ternary Operator
print("Triangle" if shape.sides() == 3 else "Square")
print('N/A' if value == None else value)

