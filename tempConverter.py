# Temp Converter

unit = input("Enter the unit of temperature (C/F): ")
temp = float(input("Enter the temperature: "))

if unit.upper() == 'C':
    converted = (temp * 9/5) + 32
    print(f'The temperature is {converted} F')

elif unit.upper() == 'F':
    converted = (temp - 32) * 5/9
    print(f'The temperature is {converted} C')

else:
    print('Invalid input')