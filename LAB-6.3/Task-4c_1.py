def sum_to_n(n):
    """
    Calculate sum of first n numbers using for loop
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# Get input from user
n = int(input("Enter a number to calculate sum of first n numbers: "))

# Calculate and display result
result = sum_to_n(n)
print(f"Sum of first {n} numbers: {result}")

# Display the calculation breakdown
print(f"\nCalculation: ", end="")
for i in range(1, n + 1):
    if i == n:
        print(f"{i} = {result}")
    else:
        print(f"{i} + ", end="")
