def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

# Take input from the user
input_string = input("Enter a string: ")


reversed_string = reverse_string(input_string)


print("Reversed string:", reversed_string)
