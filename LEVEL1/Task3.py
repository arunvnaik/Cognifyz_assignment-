def is_valid_gmail(email):
    if not email.endswith('@gmail.com'):
        return False
    
    
    local_part, domain_part = email.split('@')
    
    # Check if the local part is non-empty and does not start with a number
    if not local_part or local_part[0].isdigit():
        return False
    
    return True

# Example usage:
email = input("Enter an email address: ")
if is_valid_gmail(email):
    print(f"{email} is a valid Gmail address.")
else:
    print(f"{email} is not a valid Gmail address.")
