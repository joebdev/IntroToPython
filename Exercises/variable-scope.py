# 1. 
# Prints 20, because there are no other conditions in place to state if it's not true. 
if True:
    my_value = 20

print(my_value)

# 2. 
# Will print an error, can't access a variable before it has a value, since x is a new variable in the local scope of the function, it ignores the global x variable
# x = 10

# def my_function():
#     x = x + 5
#     print(x)

# my_function()

# 3. 
# Will print 1 to the console
def my_function():
    a = 1

    if True:
        print(a)

my_function()

# 4. 
# prints 1 to the console, it can access the global var a from inside the function
a = 1

def my_function():
    print(a)

my_function()

# 5. 
# It will print an error, because it's within local scope, and a is being defined in local scope, and it can't read the value before it's assigned
# a = 1

# # def my_function():
# #     print(a)
# #     a = 2

# # my_function()

# 6. 
# It will print 1, because the my_function isn't returning anything, and that a is a local variable compared to the global a variable
a = 1

def my_function():
    a = 2

my_function()
print(a)

# 7. 
# it will print 2, because we are accessing that 'a' variable with the global 'a' inside the function
a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# 8. 
# This will throw an error, because we can't call a variable before we define it
# print(greeting)

# greeting = 'Hello world!'

# 9. 
# 'a' will still be 7, because the integers are immutable
a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# 10. 
# This will change b[0] to be 10, lists are mutable
b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

