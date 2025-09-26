FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Loop until user enters a valid number
while True:
    try:
        input_temp = float(input("Enter the temperature to convert: "))
        break  # exit loop if input is valid
    except ValueError:
        print("Invalid input! Please enter a numeric value for the temperature.")

# Loop until user enters C or F
while True:
    conversion_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if conversion_type in ("C", "F"):
        break
    else:
        print("Invalid input! Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Perform conversion
if conversion_type == 'F':
    result = convert_to_celsius(input_temp)
    print(f"{input_temp}°F is {result:.2f}°C")
elif conversion_type == 'C':
    result = convert_to_fahrenheit(input_temp)
    print(f"{input_temp}°C is {result:.2f}°F")
