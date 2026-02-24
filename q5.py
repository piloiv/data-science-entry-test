def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Validate numeric inputs
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return False

    # Prevent division by zero
    if divisor == 0:
        return False

    # Check divisibility
    
    return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

print(check_divisibility(10, 2))
print(check_divisibility(7, 3))