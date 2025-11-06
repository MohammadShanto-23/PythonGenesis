
# Example 1: Membership operators - 'in' and 'not in'
fruits = ["apple", "banana", "mango"]

# Check if an item exists in the list
if "banana" in fruits:
    print("Banana is in the list.")

# Check if an item does not exist in the list
if "orange" not in fruits:
    print("Orange is not in the list.")

# Example 2: Using 'in' with strings
sentence = "Python is fun"
if "Python" in sentence:
    print("The word 'Python' is found in the sentence.")

# Example 3: Identity operators - 'is' and 'is not'
a = 10
b = 10
c = [1, 2, 3]
d = [1, 2, 3]

# 'is' checks if both variables refer to the same object in memory
if a is b:
    print("a and b are the same object (same memory location).")

# 'is not' checks if variables refer to different objects
if c is not d:
    print("c and d are different objects, even if their values are the same.")

# Example 4: Using 'is' with None
x = None
if x is None:
    print("x is None (no value assigned).")