def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    
    # Check if both are numeric
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1

    # Swap using arithmetic (no extra variables)
    x = x + y
    y = x - y
    x = x - y

    print("Swapped values:")
    print("x =", x)
    print("y =", y)
    
    return


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

# Task 2: Test cases

print(swap("Apple", 10))   # Should return -1
swap(9, 17)                # Should print swapped values