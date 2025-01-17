# 1. What happens when you run the following program? Why do we get that result?
# def set_foo():
#     foo = 'bar'

# set_foo()
# print(foo)

# Nothing happens with the function, nothing is returned, and trying to print foo outside of the function results in an error, because it's defined in local scope, so it's not accessible outside of the function body.


# 2. What does this program print? Why?
foo = 'bar'
def set_foo():
    foo = 'qux'
set_foo()
print(foo)

# This will print 'bar', because foo is defined in global scope, giving the print statement access to it. The function will do nothing. Nothing is returned


# 3. Write a program that uses a multiply function to multiply two numbers and returns the result. Ask the user to enter the two numbers, then output tthe numbers and result as a simple equation

def multiply():
    first = input("Enter the first number: ")
    second = input("Enter the second number: ")
    print(f"{first} * {second} = {int(first) * int(second)}")

multiply()


# 4. Consider this code:
def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

product = multiply_numbers(2, 3, 4)

# Identify the following items in that code:
    # function name <-- multiply_numbers
    # function arguments <-- 2, 3, 4
    # function definition <-- def multiply_numbers(num1, num2, num3):
    # function body <-- result = num1 * num2 * num3 && return result
    # function parameters <-- num1, num2, num3
    # function invocation <-- multiply_numbers(2, 3, 4)
    # function return value <-- return result
    # all identifiers <-- multiply_numbers, result, product, num1, num2, num3


# 5. What does the following code print?
# def scream(words):
#     return words + '!!!!'

# scream('Yipeee')

# # prints nothing, because there is no print used anywhere


# # 6. What does the following code print?def scream(words):
# def scream(words):
#     words = words + '!!!!'
#     return
#     print(words)

# scream('Yipeee')

# # prints nothing, beccause once the program has reached the return function, anything after that return is never read. 


# # 7. Without running the following code, what do you think it will do?
# def foo(bar, qux):
#     print(bar)
#     print(qux)

# foo('Hello')

# # Will throw an error for invalid argument count


# # 8. Without running the following code, what do you think it will do?
# def foo(bar, qux):
#     print(bar)
#     print(qux)

# foo(42, 3.141592, 2.718)

# # Will still give an error, for an invalid argument count


# # 9. Without running the following code, what do you think it will do?
# def foo(first, second=3, third=2):
#     print(first)
#     print(second)
#     print(third)

# foo(42, 3.141592, 2.718)

# # It will print the three values we called on line 95. 


# # 10. Without running the following code, what do you think it will do?
# def foo(first, second=3, third=2):
#     print(first)
#     print(second)
#     print(third)

# foo(42, 3.141592)

# It will print the two arguments we passed in, and then for the third argument, it'll print 2.


# Skipping all the repetitive questions, because I'm comfortable with these questions.. 

# 18. The following function returns a list of the remainders of dividing the numbers in numbers by 3:
def remainders_3(numbers):
    return [number % 3 for number in numbers]

# Use this function to determine which of the following lists contains at least one number that is not evenly divisible by 3 (that is, the remainder is not 0):
# numbers_1 = [0, 1, 2, 3, 4, 5, 6]
# numbers_2 = [1, 2, 4, 5]
# numbers_3 = [0, 3, 6]
# numbers_4 = []

# print(any(remainders_3(numbers_1)))
# print(any(remainders_3(numbers_2)))
# print(any(remainders_3(numbers_3)))
# print(any(remainders_3(numbers_4)))


# 19. The following function returns a list of the remainders of dividing the numbers in numbers by 5:
def remainders_5(numbers):
    return [number % 5 for number in numbers]

# Use this function to determine which of the following lists do not contain any numbers that are divisible by 5:
numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(all(remainders_5(numbers_1)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
print(all(remainders_5(numbers_4)))