def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

input_str = input("Enter a string: ")
print(is_palindrome(input_str))