# Terminal Output
# name = 'jane'
# print(f'Good morning, {name}!') # <-- displaying something to the terminal, giving terminal output

# Terminal Input
print("What is your name?")
name = input()
print(f"Good morning, {name}!")

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
sum = int(number1) + int(number2) # <-- When using user input, remember you must coerce and change the numbers from strings to floats or ints
print(f"The numbers {number1} and {number2} add to {sum}")