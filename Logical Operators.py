
# Example 1: Using 'and' operator
age = 20
has_id = True

if age >= 18 and has_id:
    print("You are allowed to vote.")
else:
    print("You are not allowed to vote.")

# Example 2: Using 'or' operator
is_student = False
has_discount_card = True

if is_student or has_discount_card:
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")

# Example 3: Using 'not' operator
is_raining = False

if not is_raining:
    print("You can go outside without an umbrella.")
else:
    print("Take an umbrella with you.")

# Example 4: Combining logical operators
username = "admin"
password = "1234"

if (username == "admin" and password == "1234") or (username == "guest"):
    print("Login successful.")
else:
    print("Login failed.")