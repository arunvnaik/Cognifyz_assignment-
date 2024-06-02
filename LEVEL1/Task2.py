def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Prompt the user to enter a temperature value and unit of measurement
while True:
    temp_input = input("Enter the temperature value with unit (e.g., 25C or 77F): ").strip().upper()
    
    
    if 'C' in temp_input:
        temp_value = float(temp_input.replace('C', ''))
        converted_temp = celsius_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {converted_temp:.2f}°F")
        break
    elif 'F' in temp_input:
        temp_value = float(temp_input.replace('F', ''))
        converted_temp = fahrenheit_to_celsius(temp_value)
        
        print(f"{temp_value}°F is {converted_temp:.2f}°C")
        break
    else:
        print("Invalid input. Please make sure to include the unit 'C' for Celsius or 'F' for Fahrenheit.")
