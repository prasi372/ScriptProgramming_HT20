"""
This file demonstrates call by object reference
"""
import copy

a = ['one', 'two', 'three']
b = ['one', 'two', 'three']

# Print the memory address of the variables
print(id(a))
print(id(b))

# Test if both variables are stored at the same location
print(a is b)

print("\nAssignment example--")
# Define another variable as a copy of 'a'
c = a

# Check locations
print(id(a))
print(id(c))

print("\nDeepcopy example--")
# ... yet another variable, but now using the copy method
d = copy.deepcopy(a)

# Check locations
print(id(a))
print(id(d))