from molmass import Formula
from sympy import symbols, Eq, solve
import re

def get_element_info(element_index):
    while True:
        try:
            element_symbol = input(f"Enter the symbol of element {element_index + 1} (e.g., H2 for Hydrogen): ").strip()
            element = Formula(element_symbol)
            num_sub = int(input(f"Enter the number of moles of {element_symbol} in the compound: "))
            mass = element.mass * num_sub
            print(f"The mass of {element_symbol} in the compound is {mass:.2f} g")
            return mass
        except (KeyError, ValueError):
            print("Error: Invalid element symbol or subscript. Please try again.")

def calculate_molar_mass(num_elements):
    total_mass_of_compound = 0
    for i in range(num_elements):
        mass = get_element_info(i)
        total_mass_of_compound += mass
    return total_mass_of_compound

def grams_to_moles(mass, molar_mass):
    return mass / molar_mass

def moles_to_grams(moles, molar_mass):
    return moles * molar_mass

def calculate_molarity(moles, volume):
    return moles / volume

def calculate_molality(moles, mass):
    return moles / mass

def calculate_normality(mass, equivalent_weight, volume):
    equivalents = mass / equivalent_weight
    return equivalents / volume

def calculate_percent_yield(actual_yield, theoretical_yield):
    return (actual_yield / theoretical_yield) * 100

def calculate_dilution(c1, v1, c2):
    return (c1 * v1) / c2

def balance_equation():
    print("\n--- Balance a Chemical Equation ---")
    print("Enter a chemical reaction (e.g., H2 + O2 = H2O)")
    reaction = input("Reaction: ").strip()

    try:
        from chempy import balance_stoichiometry
        reac_str, prod_str = reaction.split('=')
        reac = [r.strip() for r in reac_str.split('+')]
        prod = [p.strip() for p in prod_str.split('+')]
        reac_bal, prod_bal = balance_stoichiometry(reac, prod)

        print("\nBalanced Equation:")
        reac_part = ' + '.join(f"{v} {k}" for k, v in reac_bal.items())
        prod_part = ' + '.join(f"{v} {k}" for k, v in prod_bal.items())
        print(f"{reac_part} -> {prod_part}\n")

    except Exception as e:
        print(f"Error: {e}. Please ensure your reaction is formatted correctly.")

def get_user_choice():
    while True:
        try:
            print("\nWhat would you like to calculate?")
            print("1. Moles to grams")
            print("2. Grams to moles")
            print("3. Molarity")
            print("4. Molality")
            print("5. Normality")
            print("6. Percent Yield")
            print("7. Dilution")
            print("8. Balance Chemical Equation")
            choice = int(input("Enter the number corresponding to your choice: "))
            if choice in range(1, 9):
                return choice
            else:
                print("Invalid choice. Please select a number between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")

def main():
    choice = get_user_choice()

    if choice in [1, 2, 3, 4, 5]:
        num_elements = int(input("Enter the number of elements in the compound: "))
        molar_mass_of_compound = calculate_molar_mass(num_elements)
        print(f"The molar mass of the compound is {molar_mass_of_compound:.2f} grams/mole")

    if choice == 1:
        moles = float(input("Enter the number of moles: "))
        grams = moles_to_grams(moles, molar_mass_of_compound)
        print(f"{moles} moles of this compound is equal to {grams:.2f} grams")

    elif choice == 2:
        grams = float(input("Enter the mass in grams: "))
        moles = grams_to_moles(grams, molar_mass_of_compound)
        print(f"{grams} grams of this compound is equal to {moles:.2f} moles")

    elif choice == 3:
        molarity_moles = float(input("Enter the number of moles of solute: "))
        molarity_volume = float(input("Enter the volume of the solution in liters: "))
        final_molarity = calculate_molarity(molarity_moles, molarity_volume)
        print(f"The Molarity is {final_molarity:.2f} M")

    elif choice == 4:
        molality_moles = float(input("Enter the number of moles of solute: "))
        molality_mass = float(input("Enter the mass of the solvent in kg: "))
        final_molality = calculate_molality(molality_moles, molality_mass)
        print(f"The Molality is {final_molality:.2f} mol/kg")

    elif choice == 5:
        solute_mass = float(input("Enter the mass of the solute in grams: "))
        solution_volume = float(input("Enter the volume of the solution in liters: "))
        final_normality = calculate_normality(solute_mass, molar_mass_of_compound, solution_volume)
        print(f"The Normality is {final_normality:.2f} N")

    elif choice == 6:
        actual_yield = float(input("Enter the actual yield in grams: "))
        theoretical_yield = float(input("Enter the theoretical yield in grams: "))
        percent_yield = calculate_percent_yield(actual_yield, theoretical_yield)
        print(f"The Percent Yield is {percent_yield:.2f}%")

    elif choice == 7:
        c1 = float(input("Enter the initial concentration (C1): "))
        v1 = float(input("Enter the initial volume (V1): "))
        c2 = float(input("Enter the final concentration (C2): "))
        v2 = calculate_dilution(c1, v1, c2)
        print(f"The final volume (V2) after dilution is {v2:.2f} liters")

    elif choice == 8:
        balance_equation()

    else:
        print("Invalid choice. Please run the program again and select a valid option.")

if __name__ == "__main__":
    main()
