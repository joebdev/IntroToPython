# Variables as Pointers
numbers = [1, 2, 3, 4]
numbers[2] = 3333

x = [1, 2, 3, 4, 5]
x = [1, 2, 3] # reassigns x to the new value, does NOT mutate
x[2] = 4 # mutates the list, because it's changing the entire list

# augmented reassignments are reassignments, not mutations IF the variable references a immutable object
a = 42
b = 3.14
c = 'abc'
d = (1, 2, 3)

a *= 2
b -= 1
b /= 3
c += 'def'
d += (4, 5)

# IF augmented reassignments target a mutable object, it mutates it
a = [1, 2, 3]
b = {'a', 'b', 'c'}
a += [4, 5]
a *= 2
b -= {'b'}


# Variables and Shared Objects
numbers = [1, 2, 3]
numbers2 = numbers # Creates a new variable on the stack <-- Points to the same object in memory
print(id(numbers) == id(numbers2)) # True

# Shallow vs. Deep Copies
# Shallow Copies
# The outermost copy, so [..3, 4] is duplicated so you can change one and not the other, but the inner list is still shared between both, so changing the inner list on one, changes it on both
import copy
orig = [[1, 2], 3, 4]
dup = copy.copy(orig)

print(orig is dup) # False
print(orig == dup) # True
orig[2] = 44
print(dup)

print(orig[0] is dup[0]) # True
orig[0][1] = 22
print(dup[0])

# Deep Copies <-- Copies everything, even the nested objects
orig = [[1, 2], 3, 4]
dup = copy.deepcopy(orig)

print(orig is dup) # False
print(orig == dup) # True
orig[2] = 44
print(dup) # [[1, 2], 3, 4]
print(orig[0] is dup[0]) # False <-- orig[2] is now 44, making them different, they are no longer the same object
orig[0][1] = 22
print(dup[0]) # [1, 2]

