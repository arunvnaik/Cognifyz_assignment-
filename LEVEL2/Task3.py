import re

def password_strength(password):
    
    length = len(password) >= 8
    uppercase_char = bool(re.search(r'[A-Z]', password))
    lowercase_char = bool(re.search(r'[a-z]', password))
    digits = bool(re.search(r'\d', password))
    special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # strength score
    score = 0
    if length:
        score += 1
    if uppercase_char:
        score += 1
    if lowercase_char:
        score += 1
    if digits:
        score += 1
    if special_char:
        score += 1

    # Define strength levels
    strength_levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Good",
        3: "Strong",
        4: "Very Strong",
        5: "Excellent"
    }

    # Determine strength description
    strength_description = strength_levels[score]

    # Return result
    return {
        "score": score,
        "strength": strength_description,
        "criteria": {
            "length": length,
            "uppercase": uppercase_char,
            "lowercase": lowercase_char,
            "digit": digits,
            "special_char": special_char
        }
    }

# Example 
password = input("Enter a password to check its strength: ")
result = password_strength(password)
print(f"Password Strength: {result['strength']} (Score: {result['score']}/5)")
