FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius + CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = int(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

match unit:
    case "f":
        result = convert_to_celsius(temperature)
        print(f"{temperature}F is {result}C")
    case "c":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}C is {result}F")
    case _:
        print("Invalid temperature. Please enter a numeric value.")
