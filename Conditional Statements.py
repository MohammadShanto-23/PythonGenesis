
# Example 1: Simple if statement
num = 10
if num > 0:
    print("Number is positive.")

# Example 2: if-else statement
age = 17
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# Example 3: if-elif-else statement
marks = 75
if marks >= 80:
    print("Grade: A+")
elif marks >= 60:
    print("Grade: A")
else:
    print("Grade: B")

# Example 4: Nested if statement
x = 20
if x > 0:
    if x % 2 == 0:
        print("x is positive and even.")
    else:
        print("x is positive but odd.")
else:
    print("x is negative.")