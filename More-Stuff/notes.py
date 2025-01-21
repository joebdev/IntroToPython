# Function Composition <-- Using functions with other functions? Callbacks?
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def times(num1, num2):
    return num1 * num2

print(times(add(20, 45), subtract(80, 10))) # 4550
# 4550 == ((20 + 45) * (80 - 10))

# Method Chaining
tv_show = "Monty Python's Flying Circus"
tv_show.upper().split() # <-- Chaining multiple methods together

# datetime Module
from datetime import datetime as dt
date = dt.strptime("July 16, 2022", "%B %d, %Y")
weekday_name = date.strftime('%A')
print(weekday_name)

# Global and Nonlocal Statements
greeting = 'Salutations'

def well_howdy(who):
    global greeting # <-- Reassigns the greeting variable that is in the global scope to be the one that was made in the local scope below
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)

