# generates headings
def statement_generator(statement, decoration):  # prints statement with fancy decoration
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# displays instructions
def instructions():
    statement_generator("The ultimate conversion calculator", "_")

    print("""1. Select the conversion category
2. Enter a number
3. Enter its SI unit
4. Enter the SI unit that you want to convert it to""")


def float_check(question):  # check if user quits. if not, check that input is a number
    error = "Error: Please enter a number over zero (could include decimals)\n"
    while True:
        response = input(question)

        try:
            # convert input to float
            response = float(response)
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            # prevent user from inputting string for the number
            print(error)


def unit_check(unit):
    error = f"Error: unit type not found in the {category} category."

    while True:
        response = input(unit)

        # sort what units belong in what categories
        if category == "distance":
            if response.lower() in distance_units:
                print("Unit found!")
                return response.lower()
            else:
                print(error, "\n")
        elif category == "mass":
            if response.lower() in mass_units:
                print("Unit found!")
                return response.lower()
            else:
                print(error, "\n")
        elif category == "time":
            if response.lower() in time_units:
                print("Unit found!")
                return response.lower()
            else:
                print(error, "\n")
        elif category == "volume":
            if response.lower() in volume_units:
                print("Unit found!")
                return response.lower()
            elif response in volume_units_2:
                print("Unit found!")
                return response
            else:
                print(error)
                print("Volume measurement units can be case sensitive: mL, L, kL, ML\n")


def unit_convert(amount, si_old, si_new):
    if category == "distance":
        # convert original unit into a standard unit using multiplication
        multiply = distance_units[si_new]
        standard = amount * multiply

        # divide to get desired unit (unit_new)
        divide = distance_units[si_old]
        result = standard / divide

    elif category == "mass":
        # convert original unit into a standard unit using multiplication
        multiply = mass_units[si_new]
        standard = amount * multiply

        # divide to get desired unit (unit_new)
        divide = mass_units[si_old]
        result = standard / divide

    elif category == "time":
        # convert original unit into a standard unit using multiplication
        multiply = time_units[si_new]
        standard = amount * multiply

        # divide to get desired unit (unit_new)
        divide = time_units[si_old]
        result = standard / divide

    elif category == "volume":
        if si_new in volume_units:
            # check which dictionary si_new is in
            multiply = volume_units[si_new]
        else:
            multiply = volume_units_2[si_new]
        standard = amount * multiply

        # check which dictionary si_old is in
        if si_old in volume_units:
            divide = volume_units[si_old]
        else:
            divide = volume_units_2[si_old]
        result = standard / divide

    return result


# Main routine
category_list = ["distance", "mass", "time", "volume"]

# dictionaries with units for different categories
distance_units = {
    "millimetres": 1000,
    "mm": 1000,
    "centimetres": 100,
    "cm": 100,
    "metres": 1,
    "m": 1,
    "kilometres": 0.001,
    "km": 0.001
}

mass_units = {
    "milligrams": 1000,
    "mg": 1000,
    "grams": 1,
    "g": 1,
    "kilograms": 0.001,
    "kg": 0.001,
    "tonnes": 0.000001,
    "t": 0.000001
}

time_units = {
    "milliseconds": 60000,
    "ms": 60000,
    "seconds": 60,
    "s": 60,
    "minutes": 1,
    "min": 1,
    "hours": 0.01666666666666666666666666666667,
    "h": 0.01666666666666666666666666666667,
    "days": 6.9444444444444444444444444444444e-4,
    "years": 1.9012852688417370142216138109362e-6
}

volume_units = {
    "millilitres": 1000,
    "litres": 1,
    "kilolitres": 0.001,
    "megalitres": 0.000001
}

# this dictionary is case-sensitive
volume_units_2 = {
    "mL": 1000,
    "L": 1,
    "kL": 0.001,
    "ML": 0.000001
}

want_instructions = input("Press <enter> to read the instructions or any key to continue ")

if want_instructions == "":
    instructions()

while True:

    print("---")
    # get user input
    category = input("Select category: Distance, mass, time, or volume:\n(Press 'xxx' to quit) ").lower()
    while category not in category_list:
        if category == "xxx":  # check if user quits
            print("Bye bye :D")
            quit()
        print("Error: category not recognised.\n")
        category = input("Select category: Distance, mass, time, or volume:\n(Press 'xxx' to quit) ").lower()

    print("---")
    number = float_check("Enter number: ")
    print("---")
    unit_old = unit_check("What unit is it in? ")
    print("---")
    unit_new = unit_check("Convert to? ")
    print("---")

    convert = unit_convert(number, unit_old, unit_new)
    print(f"{number} {unit_old} is {convert} {unit_new}")
