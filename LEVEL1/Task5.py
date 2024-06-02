def is_palindrome(s):
    s = s.replace('  ','').lower().strip()
    return s == s[::-1]

# Example usage:
input_str = input("Enter a string to check if it's a palindrome: ")
print(is_palindrome(input_str))
