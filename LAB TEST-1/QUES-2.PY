from typing import Iterable, Tuple

def sum_even_odd(numbers: Iterable[int]) -> Tuple[int, int]:
    """Return a tuple (sum_of_even_numbers, sum_of_odd_numbers).

    Non-integer values in the iterable will raise a TypeError.
    """
    even_sum = 0
    odd_sum = 0
    for value in numbers:
        if not isinstance(value, int):
            raise TypeError("sum_even_odd expects an iterable of integers")
        if value % 2 == 0:
            even_sum += value
        else:
            odd_sum += value
    return even_sum, odd_sum


if __name__ == "__main__":
    print("Enter integers separated by spaces:")
    try:
        parts = input().strip().split()
        values = [int(p) for p in parts]
    except ValueError:
        print("Invalid input. Please enter integers only.")
    else:
        even_sum, odd_sum = sum_even_odd(values)
        print(f"Sum of even numbers: {even_sum}")
        print(f"Sum of odd numbers : {odd_sum}")


