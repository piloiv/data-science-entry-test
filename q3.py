def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    
    # Validate input type
    if not isinstance(dct, dict):
        return -1

    # Check if key exists
    if key in dct:
        print("Original value:", dct[key])

    # Update / Add key-value pair
    dct[key] = value

    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

print(update_dictionary({}, "name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))