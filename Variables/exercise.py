# 1. Classify the following potential non-constant variable names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.
    # index # idiomatic
    # CatName # non-idiomatic <-- shouldn't use upper camelcase for variable names
    # lazy_dog # idiomatic
    # quick_Fox # non-idiomatic <-- should use all lowercase for variable names
    # 1stCharacter # illegal <-- can't start with a number
    # operand2 # idiomatic
    # BIG_NUMBER # non-idiomatic <-- should only be used for constants
    # π # non-idiomatic <-- shouldn't use symbols as variable names

# 2. Classify the following potential function names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.
    # index # idiomatic
    # CatName # non-idiomatic <-- Shouldn't use UpperCamelCase
    # lazy_dog # idiomatic
    # quick_Fox # non-idiomatic <-- use lower case letters
    # 1stCharacter # illegal <-- can't start with a number
    # operand2 # idiomatic
    # BIG_NUMBER #non-idiomatic <-- should only be used for constants
    # π # non-idiomatic <-- shouldn't use symbols as variable names

# 3. Classify the following potential constant names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.
    # index # non-idiomatic <-- should use all capital letters
    # CatName # non-idiomatic <-- Needs to be all capital letters
    # LAZY_DOG3 # idiomatic
    # quick_Fox # non-idiomatic <-- Should be all capital letters
    # 1ST # illegal <-- can't start with a number
    # operand2 # non-idiomatic <-- needs to be all capital letters
    # BIG_NUMBER #idiomatic
    # π # non-idiomatic <-- shouldn't use symbols as variable names

# 4. Classify the following potential class names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.
    # index # non-idiomatic <-- should use PascalCase
    # CatName # idiomatic
    # Lazy_Dog # non-idiomatic <-- needs PascalCase and no underscores
    # 1ST # illegal <-- can't start with numbers
    # operand2 # non-idiomatic <-- should use PascalCase
    # BigNumber3 # idiomatic
    # Πi # non-idiomatic <-- shouldn't use symbols as variable names

# 5. Write a program named greeter.py that greets 'Victor' three times. Your program should use a variable and not hard code the string 'Victor' in each greeting. 
name = 'Victor'
print(f'Good morning, {name}.')
print(f'Good afternoon, {name}.')
print(f'Good evening, {name}.')

# 6. Write a program named age.py that includes someone's age and then calculates and reports the future age 10, 20, 30, and 40 years from now. 
age = 31
print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')

# 7. What happens when you run the following code? Why?
# It will first greet Victor all three times, and then reassign NAME to Nina, and greet Nina all three times, since Constants can be reassigned in Python.
NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

# 8. Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays you 5% (this is a wish-fulfillment fantasy) compounded interest every year. 
# After one year, you will have $1,050 ($1,000 times 1.05). After two years, you will have $1,050 times 1.05, or $1102.50. 
# Create a variable named balance that contains the amount of money you will have after 5 years, then print the result. Use a single expression if you can to set balance to the correct value.

balance = 1000 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05

print(balance)

# 9. Repeat the previous question but, this time, use augmented assignment to compute the final result, one year at a time
aug_balance = 1000
aug_balance *= 1.05
aug_balance *= 1.05
aug_balance *= 1.05
aug_balance *= 1.05
aug_balance *= 1.05
print(aug_balance)

# 10. Assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statments reassign the variable? Which statements mutate the value of the object that obj references?
# Which statements do neither? 
obj = 'ABcd' # reassign
obj.upper() # neither
obj = obj.lower() # mutates <-- should be reassignment
print(len(obj)) # neither
obj = list(obj) # mutates <-- should be reassignment
obj.pop() # neither <-- should be mutate
obj[2] = 'X' # mutates
obj.sort() # neither <-- should be mutate
set(obj) # mutates <-- should be neither
obj = tuple(obj) # mutates <-- should be reassignment
