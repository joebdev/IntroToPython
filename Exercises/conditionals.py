# 1. 
    # 0
    # None
    # False
    # [], {}, (), set(), range(0), ''

# 2. 
import random
random_number = random.randint(0, 1)
if random_number:
    print('Yes!')
else:
    print('No')

# 3. 
print('Yes!') if random_number else print("No")

# 4. 
weather = 'sunny'
if weather == 'sunny':
    print("It's a beautiful day!")
elif weather == 'rainy':
    print("Grab your umbrella")
else:
    print("Let's stay inside")

# 5. 
animal = 'horse'
# will print 'neigh'
match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh')
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')

# 6. 
match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrella")
    case 'snowy':
        print("Better wear your coat")
    case _:
        print("Better stay inside!")

# 7. 
# will print 'Yes!'
if False or True:
    print('Yes!')
else:
    print('No...')

# 8. 
# will print 'No...'
if True and False:
    print('Yes!')
else:
    print('No...')

# 9. 
sale = True
admission_price = 5.25 if not sale else 3.99
print(f'${admission_price}')

# 10.
# True
speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)