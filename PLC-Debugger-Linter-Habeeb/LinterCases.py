#Generated by 4o

# Test 1: Function name should be snake_case
def AddNumbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b


# Test 2: Variable names should be lowercase
def compute_sum():
    Total = 0  # Incorrect variable name
    for i in range(10):
        Total += i
    return Total


# Test 3: Unused variables should be flagged
def calculate_area(radius):
    pi = 3.14
    unused_variable = 100  # This variable is unused
    return pi * radius * radius


# Test 5: Division by zero check
def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def divide_by_constant(a):
    return a / 0  # Linter should flag this as division by zero


# Test 6: Uninitialized variables
def calculate_sum():
    total += 10  # total is used before being initialized
    return total


# Test 7: Infinite loop warning
def infinite_loop():
    i = 0
    while i >= 0:  # This is likely to run forever
        i -= 1

# Test 9: Unreachable code
def check_unreachable_code():
    return "This is returned"
    print("This will never be executed")  # Unreachable code
