# 1. Write a program named greeter.py. The program should ask you for your name, then output Hello, NAME! where name is the name you entered
# name = input("What is your name? ")
# print(f"Hello, {name}!")

# 2. Modify the greeter.py to ask for the user's first and last names separately, then greet the user with their full name
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print(f"Hello, {first_name} {last_name}!")

# 3. Write a program named age.py that asks the user to enter their age, then calculates and reports the future age 10, 20, 30 and 40 years from now
age = input("What is your current age? ")
print(f'You are {age} years old.')
print(f'In 10 years, you will be {int(age) + 10} years old.')
print(f'In 20 years, you will be {int(age) + 20} years old.')
print(f'In 30 years, you will be {int(age) + 30} years old.')
print(f'In 40 years, you will be {int(age) + 40} years old.')