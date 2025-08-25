def validate_indian_mobile(mobile_number):
    """
    Validate an Indian mobile number
    Args:
        mobile_number (str): The mobile number to validate   
    Returns:
        bool: True if valid, False otherwis
    Rules:
        - Must be exactly 10 digits long
        - Must start with 6, 7, 8, or 9
    """
    # Remove any spaces or special characters
    cleaned_number = ''.join(filter(str.isdigit, str(mobile_number)))
    # Check if the number is exactly 10 digits
    if len(cleaned_number) != 10:
        return False
    # Check if the number starts with 6, 7, 8, or 9
    if not cleaned_number[0] in ['6', '7', '8', '9']:
        return False
    return True
# Test cases
if __name__ == "__main__":
    # Valid numbers
    print("Valid numbers:")
    print(validate_indian_mobile("9876543210"))  # True
    print(validate_indian_mobile("8765432109"))  # True
    print(validate_indian_mobile("7654321098"))  # True
    print(validate_indian_mobile("6543210987"))  # True
    # Invalid numbers
    print("\nInvalid numbers:")
    print(validate_indian_mobile("1234567890"))  # False (starts with 1)
    print(validate_indian_mobile("987654321"))   # False (9 digits)
    print(validate_indian_mobile("98765432101")) # False (11 digits)
    print(validate_indian_mobile("987654321a"))  # False (contains letter)
    print(validate_indian_mobile(""))            # False (empty)
    print(validate_indian_mobile("98765 43210")) # False (with spaces)

