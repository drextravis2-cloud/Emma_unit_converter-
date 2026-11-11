"""
Engineering Unit Converter
Converts between mm/inches, C/F, kg/lb and km/h / m/s.
Own twist: the program keeps a conversion history that you can view
during the session (menu option 9).
"""

# ---------- Conversion functions ----------
# Each function takes one number and returns the converted number.

def mm_to_inch(value):
    return value / 25.4

def inch_to_mm(value):
    return value * 25.4

def c_to_f(value):
    return value * 9 / 5 + 32

def f_to_c(value):
    return (value - 32) * 5 / 9

def kg_to_lb(value):
    return value * 2.20462

def lb_to_kg(value):
    return value / 2.20462

def kmh_to_ms(value):
    return value / 3.6

def ms_to_kmh(value):
    return value * 3.6


# Menu table: choice -> (from unit, to unit, function to use)
CONVERSIONS = {
    "1": ("mm", "inches", mm_to_inch),
    "2": ("inches", "mm", inch_to_mm),
    "3": ("°C", "°F", c_to_f),
    "4": ("°F", "°C", f_to_c),
    "5": ("kg", "lb", kg_to_lb),
    "6": ("lb", "kg", lb_to_kg),
    "7": ("km/h", "m/s", kmh_to_ms),
    "8": ("m/s", "km/h", ms_to_kmh),
}


def show_menu():
    """Print the main menu."""
    print("\n===== ENGINEERING UNIT CONVERTER =====")
    for key, (from_unit, to_unit, _) in CONVERSIONS.items():
        print(f"{key}. {from_unit} to {to_unit}")
    print("9. View conversion history")
    print("0. Quit")


def get_number(prompt):
    """Keep asking until the user types a valid number."""
    while True:
        text = input(prompt)
        try:
            return float(text)  # convert the text to a decimal number
        except ValueError:
            # Runs if the user typed letters or symbols instead of a number
            print("Invalid input. Please type a number, e.g. 25 or 3.5")


def show_history(history):
    """Print every conversion done so far (my own twist)."""
    if len(history) == 0:
        print("No conversions yet.")
    else:
        print("\n--- Conversion history ---")
        for number, entry in enumerate(history, start=1):
            print(f"{number}. {entry}")


def main():
    history = []  # list that stores each conversion as text

    # Main loop: repeats until the user chooses 0
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "9":
            show_history(history)
        elif choice in CONVERSIONS:
            from_unit, to_unit, convert = CONVERSIONS[choice]
            value = get_number(f"Enter value in {from_unit}: ")

            # Absolute zero check so impossible temperatures are rejected
            if choice == "3" and value < -273.15:
                print("Error: below absolute zero (-273.15 °C).")
            elif choice == "4" and value < -459.67:
                print("Error: below absolute zero (-459.67 °F).")
            elif choice in ("1", "2", "5", "6") and value < 0:
                print("Error: length and mass cannot be negative.")
            else:
                result = convert(value)
                line = f"{value:g} {from_unit} = {result:.4f} {to_unit}"
                print("Result:", line)
                history.append(line)  # save to history
        else:
            print("Invalid choice. Please pick a number from the menu.")


# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()
