# 1. 
for num in range(0, 11, 2):
    print(num)

# 2. 
for num in range(10, -1, -1):
    if num == 0:
        print('Launch!')
    else:
        print(num)

# 3. 
greeting = 'Aloha'
count = 0

while count < 3:
    print(greeting)
    count += 1

# 4. 
for i in range(1, 101):
    print(i * 2)

# 5. 
lst = [1, 3, 7, 15]
count = 0
while count < len(lst):
    print(lst[count])
    count += 1

# 6. 
friends = ['Sarah', 'John', 'Hannah', 'Dave']
greeting = 'Hello'
for friend in friends:
    print(f'{greeting}, {friend}!')

# 7.
cities = ['Istanbul', 'Los Angeles', 'Tokyo', None, 'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city is None:
        continue
    else:
        print(len(city))

# 8.
while True:
    print('and on')
    break

# 9. 
fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print(fish)
    if fish == 'Nemo':
        break

# 10. 
while True:
    print('Should I stop logging?')
    answer = input()
    if answer == 'yes':
        break