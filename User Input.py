
print("Welcome to the User Info & Calculator Program!\n")

# User input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

# Numbers input 
print("\nNow, let's enter three numbers for calculation.")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Calculation
total = num1 + num2 + num3
average = total / 3

# Output display
print("\n----- Summary -----")
print(f"Hello {name} from {city}, age {age}!")
print(f"You entered numbers: {num1}, {num2}, {num3}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print("-------------------")

