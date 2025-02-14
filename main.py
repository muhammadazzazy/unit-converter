from sys import exit


def convert_temp(value: float, unit_from: str, unit_to: str, temp_units: list[str]) -> float:
    if unit_from == temp_units[0] and unit_to == temp_units[1]:
        temperature_celsius: float = value - 273.15
        return temperature_celsius

    elif unit_from == temp_units[0] and unit_to == temp_units[2]:
        temperature_celsius: float = value - 273.15
        temperature_fahrenheit: float = (temperature_celsius * 9/5) + 32
        return temperature_fahrenheit

    elif unit_from == temp_units[1] and unit_to == temp_units[0]:
        temperature_kelvin: float = value + 273.15
        return temperature_kelvin

    elif unit_from == temp_units[1] and unit_to == temp_units[2]:
        temperature_fahrenheit: float = (value * 9/5) + 32
        return temperature_fahrenheit

    elif unit_from == temp_units[2] and unit_to == temp_units[1]:
        temperature_celsius: float = (5/9) * (value - 32)
        return temperature_celsius

    elif unit_from == temp_units[2] and unit_to == temp_units[0]:
        temperature_celsius: float = (5/9) * (value - 32)
        temperature_kelvin: float = temperature_celsius + 273.15
        return temperature_kelvin


def convert_vol(value: float, unit_from: str, unit_to: str, vol_units: list[str]) -> float:
    if unit_from == vol_units[0] and unit_to == vol_units[1]:
        volume_liters = value * pow(10, 3)
        return volume_liters

    elif unit_from == vol_units[0] and unit_to == vol_units[2]:
        volume_deciliters = value * pow(10, 4)
        return volume_deciliters

    elif unit_from == vol_units[0] and (unit_to == [3] or unit_to == vol_units[4]):
        volume_milliliters = value * pow(10, 6)
        return volume_milliliters

    elif unit_from == vol_units[1] and unit_to == vol_units[0]:
        volume_cubic_meters = value / pow(10, 3)
        return volume_cubic_meters

    elif unit_from == vol_units[1] and unit_to == vol_units[2]:
        volume_deciliters = value * pow(10, 1)
        return volume_deciliters

    elif unit_from == vol_units[1] and (unit_to == vol_units[3] or unit_to == vol_units[4]):
        volume_milliliters = value * pow(10, 3)
        return volume_milliliters

    elif unit_from == vol_units[2] and unit_to == vol_units[0]:
        volume_cubic_meters = value / pow(10, 4)
        return volume_cubic_meters

    elif unit_from == vol_units[2] and unit_to == vol_units[1]:
        volume_liters = value / pow(10, 1)
        return volume_liters

    elif unit_from == vol_units[2] and (unit_to == vol_units[3] or unit_to == vol_units[4]):
        volume_milliliters = value * pow(10, 2)
        return volume_milliliters

    elif (unit_from == vol_units[3] or unit_from == vol_units[4]) and unit_to == vol_units[0]:
        volume_cubic_meters = value / pow(10, 6)
        return volume_cubic_meters

    elif (unit_from == vol_units[3] or unit_from == vol_units[4]) and unit_to == vol_units[1]:
        volume_liters = value / pow(10, 3)
        return volume_liters

    elif (unit_from == vol_units[3] or unit_from == vol_units[4]) and unit_to == vol_units[2]:
        volume_deciliters = value / pow(10, 2)
        return volume_deciliters

    elif (unit_from == vol_units[3] or unit_from == vol_units[4]) and (unit_to == vol_units[3] or unit_to == vol_units[4]):
        return value


def convert_mass(value: float, unit_from: str, unit_to: str, mass_units: list[str]) -> float:
    if (unit_from == mass_units[0]) and (unit_to == mass_units[1]):
        mass_kilograms = value * pow(10, 3)
        return mass_kilograms

    elif (unit_from == mass_units[0]) and (unit_to == mass_units[2]):
        mass_grams = value * pow(10, 6)
        return mass_grams

    elif (unit_from == mass_units[0]) and (unit_to == mass_units[3]):
        mass_milligrams = value * pow(10, 9)
        return mass_milligrams

    elif (unit_from == mass_units[1]) and (unit_to == mass_units[0]):
        mass_tonnes = value / pow(10, 3)
        return mass_tonnes

    elif (unit_from == mass_units[1]) and (unit_to == mass_units[2]):
        mass_grams = value * pow(10, 3)
        return mass_grams

    elif (unit_from == mass_units[1]) and (unit_to == mass_units[3]):
        mass_milligrams = value * pow(10, 6)
        return mass_milligrams

    elif (unit_from == mass_units[2]) and (unit_to == mass_units[0]):
        mass_tonnes = value / pow(10, 6)
        return mass_tonnes

    elif (unit_from == mass_units[2]) and (unit_to == mass_units[1]):
        mass_kilograms = value / pow(10, 3)
        return mass_kilograms

    elif (unit_from == mass_units[2]) and (unit_to == mass_units[3]):
        mass_milligrams = value * pow(10, 3)
        return mass_milligrams

    elif (unit_from == mass_units[3]) and (unit_to == mass_units[0]):
        mass_tonnes = value / pow(10, 9)
        return mass_tonnes

    elif (unit_from == mass_units[3]) and (unit_to == mass_units[1]):
        mass_kilograms = value / pow(10, 6)
        return mass_kilograms

    elif (unit_from == mass_units[3]) and (unit_to == mass_units[2]):
        mass_grams = value / pow(10, 3)
        return mass_grams


def main() -> None:
    greeting: str = """Welcome to The Unit Converter!
Supported quantities and units:
\tTemperature: Kelvin, Degree Celsius, Degree Fahrenheit
\tVolume: m^3, L, dL, mL, cm^3
\tMass: ton, kg, g, mg
"""
    print(greeting)

    units: dict = {'temperature': ['Kelvin', 'Degree Celsius', 'Degree Fahrenheit'],
                   'volume': ['m^3', 'L', 'dL', 'mL', 'cm^3'],
                   'mass': ['ton', 'kg', 'g', 'mg']}
    while True:
        try:
            user_input = input('Enter the type of unit to convert from: ')

            if user_input == 'exit':
                print('Thanks for trying my program!')
                exit()

            unit_from = user_input

            if unit_from not in units['temperature'] and unit_from not in units['mass'] and unit_from not in units['volume']:
                print('Invalid unit...')
                continue

            unit_to = input('Enter the type of unit to convert to: ')

            if unit_to not in units['temperature'] and unit_to not in units['mass'] and unit_to not in units['volume']:
                print('Invalid unit...')
                continue

            if unit_from == unit_to:
                print('Same unit...')
                continue

            flag = False
            for key in units.keys():
                if unit_from in units[key] and unit_to in units[key]:
                    flag = True
                    break

            if not flag:
                print('Units do not belong to the same quantity...')
                continue

            value: float = float(input('Enter the value: '))

            if key == 'temperature':
                temp = convert_temp(
                    value, unit_from, unit_to, units['temperature'])
                print(f'{value:.2f} {unit_from} = {temp:.2f} {unit_to}')
            elif key == 'volume':
                vol = convert_vol(value, unit_from, unit_to, units['volume'])
                print(f'{value:.2f} {unit_from} = {vol:.2f} {unit_to}')
            elif key == 'mass':
                mass = convert_mass(value, unit_from, unit_to, units['mass'])
                print(f'{value:.2f} {unit_from} = {mass:.2f} {unit_to}')

        except ValueError:
            print('Invalid input...')
            continue
        except KeyboardInterrupt:
            print('Exiting...')
            exit()


if __name__ == '__main__':
    main()
