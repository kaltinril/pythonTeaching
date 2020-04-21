valid_units = ['C', 'F', 'K']


# C to F: Divide by 5, then multiply by 9, then add 32
def celsius_to_fahrenheit(c):
    return ((c / 5) * 9) + 32


# F to C: Deduct 32, then multiply by 5, then divide by 9
def fahrenheit_to_celsius(f):
    return ((f - 32) * 5) / 9


# C to K: add 273.15
def celsius_to_kelvin(c):
    return c + 273.15


# K to C: subtract 273.15
def kelvin_to_celsius(k):
    return k - 273.15


# F to K: Deduct 32, then multiply by 5, then divide by 9, add 273.15
def fahrenheit_to_kelvin(f):
    c = fahrenheit_to_celsius(f)
    return celsius_to_kelvin(c)


# K to F: Deduct 273.15, Divide by 5, then multiply by 9, then add 32
def kelvin_to_fahrenheit(k):
    c = kelvin_to_celsius(k)
    return celsius_to_fahrenheit(c)


def get_from_unit(units):
    valid = False
    return_value = 'n'
    while not valid:
        return_value = input('Convert from [C]elsius, [F]ahrenheit, or [K]elvin? ').upper()
        if return_value in units:
            valid = True
        else:
            print('Invalid: Enter one of these: ', units)

    return return_value


def get_to_unit(units, start_value):
    # We shouldn't be able to select FROM and TO as the same unit type.
    # Meaning, if we are converting FROM Celsius, we shouldn't allow converting TO Celsius.
    remaining = units.copy()
    remaining.remove(start_value)

    valid = False
    return_value = 'n'
    while not valid:
        return_value = input('Convert to [C]elsius, [F]ahrenheit, or [K]elvin? ').upper()
        if return_value in remaining:
            valid = True
        else:
            print('Invalid: Enter either of these: ', remaining)

    return return_value


def get_from_value(from_unit):
    return float(input('Enter the temperature in ' + from_unit))


def check_and_convert(from_unit, to_unit, start_value):
    result = 0.0
    if from_unit == 'C':
        if to_unit == 'F':
            result = celsius_to_fahrenheit(start_value)
        elif to_unit == 'K':
            result = celsius_to_kelvin(start_value)
        else:
            result = 'Unknown unit type to convert from: ' + to_unit
    elif from_unit == 'F':
        if to_unit == 'C':
            result = fahrenheit_to_celsius(start_value)
        elif to_unit == 'K':
            result = fahrenheit_to_kelvin(start_value)
        else:
            result = 'Unknown unit type to convert from: ' + to_unit
    elif from_unit == 'K':
        if to_unit == 'C':
            result = kelvin_to_celsius(start_value)
        elif to_unit == 'F':
            result = kelvin_to_fahrenheit(start_value)
        else:
            result = 'Unknown unit type to convert from: ' + to_unit
    else:
        result = 'Unknown unit type to convert from: ' + from_unit

    return result


def print_results(to_unit, end_value):
    print('Conversion to ' + to_unit + ' is ' + str(end_value))


def do_another_conversion():
    keep_going = input('Do another conversion Y/N? ').upper()
    return keep_going == 'Y'


still_running = True
while still_running:
    # 1. This program will ask the user for what they want to convert from and to.
    convert_from = get_from_unit(valid_units)
    convert_to = get_to_unit(valid_units, convert_from)
    from_value = get_from_value(convert_from)

    # 2. It will then call the appropriate function
    to_value = check_and_convert(convert_from, convert_to, from_value)

    # 3. It will print out the results for the user to see.
    print_results(convert_to, to_value)

    # 4. The program will loop until the user presses Q, allowing them to pick a new conversion.
    still_running = do_another_conversion()
