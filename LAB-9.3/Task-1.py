def sum_even_odd(numbers):                # Define a function to calculate sums of even and odd numbers
    even_sum = 0                          # Initialize sum for even numbers
    odd_sum = 0                           # Initialize sum for odd numbers
    for num in numbers:                   # Loop through each number in the list
        if num % 2 == 0:                  # Check if the number is even
            even_sum += num               # Add even number to even_sum
        else:                             # If the number is odd
            odd_sum += num                # Add odd number to odd_sum
    return even_sum, odd_sum              # Return both sums as a tuple

# Get input from user
user_input = input("Enter numbers separated by spaces: ")  # Prompt user to enter numbers
nums = [int(x) for x in user_input.split()]                # Split input and convert each part to integer
even, odd = sum_even_odd(nums)                             # Call function and get sums
print("Sum of even numbers:", even)                        # Print sum of even numbers
print("Sum of odd numbers:", odd)                          # Print sum of odd numbers