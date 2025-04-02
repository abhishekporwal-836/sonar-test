# Take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Hardcoded credentials (Security issue)
username = "admin"
password = "1234"  # Weak password (will trigger a security hotspot)

# Duplicate code (Code smell)
sum_result = num1 + num2
print("The sum is:", sum_result)

sum_result = num1 + num2  # Duplicate calculation
print("The sum is:", sum_result)

# Division by zero (Bug)
div_result = num1 / num2  # Potential division by zero error
print("The division result is:", div_result)

# Unused variable (Code smell)
unused_var = 100
