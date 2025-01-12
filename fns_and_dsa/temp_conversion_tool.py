# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Conversion factor for Celsius to Fahrenheit

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): The temperature in Fahrenheit.

    Returns:
    float: The temperature converted to Celsius.
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.

    Parameters:
    celsius (float): The temperature in Celsius.

    Returns:
    float: The temperature converted to Fahrenheit.
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main function for user interaction
def main():
    inputs = [
        ("Enter the temperature to convert: ", "37.5"),
        ("Is this temperature in Celsius or Fahrenheit? (C/F): ", "C"),
        ("Would you like to convert another temperature? (yes/no): ", "no"),
    ]
    input_iterator = iter(inputs)

    def mock_input(prompt):
        print(prompt)
        response = next(input_iterator)[1]
        print(response)
        return response

    # Replace built-in input with the mock_input for testing
    global input
    input = mock_input

    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'F':
                converted = convert_to_celsius(temperature)
                print(f"{temperature:.2f}°F is {converted:.2f}°C")
            elif unit == 'C':
                converted = convert_to_fahrenheit(temperature)
                print(f"{temperature:.2f}°C is {converted:.2f}°F")
            else:
                print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

            another = input("Would you like to convert another temperature? (yes/no): ").strip().lower()
            if another != 'yes':
                print("Goodbye!")
                break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
