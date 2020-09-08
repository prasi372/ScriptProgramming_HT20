"""
This file demonstrates call by object reference
"""

a = "test"
b = "test"

# Try with floats/ints if you like
#a = 5.5
#b = 5.5

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
