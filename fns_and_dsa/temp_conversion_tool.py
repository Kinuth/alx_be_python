FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def covert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.

    Returns:
    float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    Parameters:
    celsius (float): Temperature in Celsius.

    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

input_temp = float(input("Enter the temperature to convert: "))
conversion_type = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()
if conversion_type == 'F':
    result = covert_to_celsius(input_temp)
    print(f"{input_temp}°F is {result:.2f}°C")
elif conversion_type == 'C':
    result = convert_to_fahrenheit(input_temp)
    print(f"{input_temp}°C is {result:.2f}°F")