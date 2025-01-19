# 1. To what values do the following expressions evaluate?
False or (True and False) # False
True or (1 + 2) # True
(1 + 2) or True # True
True and (1 + 2) # True
False and (1 + 2) # False
(1 + 2) and True # True
(32 * 4) >= 129 # True
False != (not True) # False
True == 4 # False
False == (847 == '847') # True

# 2. Write a function, even_or_odd, that determines whether its argument is an even or odd number. If it's even, the function should print 'even'; otherwise, it should print 'odd'
def even_or_odd(num):
    if num % 2 == 0:
        print('even')
    else:
        print('odd')
    # print('even' if num % 2 == 0 else print('odd'))

even_or_odd(4)

# 3. Without running the following code, what does it print? Why?
def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113') # Product2
bar_code_scanner(142) # Product not found!, because 142 does not equal '142'

# 4. Refactor this code to use a regular if statement instead
# return ('bar' if foo() else qux())
# if foo():
#     return 'bar'
# else:
#     return qux()

# 5. What does this code output, and why?
def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([]) # outputs 'Empty' because the list is empty, so it's a falsy value

# 6. Write a function that takes a string as an argument and returns an all-caps version of the string when the string is longer than 10 characters. Otherwise, it should return the original string.
def check_str(str):
    if len(str) > 10:
        print(str.upper())
    else:
        print(str)

check_str('hello')

# 7. Write a function that takes a single integer argument and prints a message that describes whether:
    # The value is between 0 and 50 (inclusive)
    # The value is between 51 and 100 (inclusive)
    # The value is greater than 100
    # The value is less than 0

def check_value(num):
    if num >= 0 and num <= 50:
        print(f'{num} is between 0 and 50')
    elif num >= 51 and num <= 100:
        print(f'{num} is between 51 and 100')
    elif num > 100:
        print(f'{num} is greater than 100')
    else:
        print(f'{num} is less than 0')

check_value(0)     # 0 is between 0 and 50
check_value(25)    # 25 is between 0 and 50
check_value(50)    # 50 is between 0 and 50
check_value(75)    # 75 is between 51 and 100
check_value(100)   # 100 is between 51 and 100
check_value(101)   # 101 is greater than 100
check_value(-1)    # -1 is less than 0