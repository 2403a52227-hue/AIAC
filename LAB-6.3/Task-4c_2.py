def sum_to_n_while(n):
    """
    Calculate sum of first n numbers using while loop
    """
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total
# Get input from user
n = int(input("Enter a number to calculate sum of first n numbers: "))
# Calculate and display result
result = sum_to_n_while(n)
print(f"Sum of first {n} numbers: {result}")
# Display the calculation breakdown using while loop
print(f"\nCalculation: ", end="")
i = 1
while i <= n:
    if i == n:
        print(f"{i} = {result}")
    else:
        print(f"{i} + ", end="")
    i += 1