def factorial(n):
    """
    Calculate the factorial of a number.
    Args:
        n (int): The number to calculate factorial for
    Returns:
        int or str: Factorial result or error message
    Rules:
        - If n is negative, return error message
        - If n is 0, return 1
        - For positive n, return n!
    """
    # Check for negative numbers
    if n < 0:
        return "Factorial is not defined for negative numbers."
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Calculate factorial for positive numbers
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Main program with user input
if __name__ == "__main__":
    print("Factorial Calculator")
    print("=" * 20)
    try:
        # Get user input
        user_input = input("Enter a number to calculate factorial: ")
        number = int(user_input)
        # Calculate and display result
        result = factorial(number)
        print(f"\nFactorial of {number} = {result}")
    except ValueError:
        print("Error: Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
