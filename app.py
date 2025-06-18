from chemcalc.core import *

def get_user_choice():
    print("\nWhat would you like to calculate?")
    print("1. Moles to grams")
    print("2. Grams to moles")
    print("3. Molarity")
    print("4. Molality")
    print("5. Normality")
    print("6. Percent Yield")
    print("7. Dilution")
    print("8. Balance Chemical Equation")
    return int(input("Enter the number corresponding to your choice: "))

def main():
    choice = get_user_choice()

    if choice in [1, 2, 3, 4, 5]:
        num_elements = int(input("Enter number of elements in the compound: "))
        molar_mass = calculate_molar_mass(num_elements)
        print(f"Molar Mass: {molar_mass:.2f} g/mol")

    if choice == 1:
        moles = float(input("Enter moles: "))
        print(f"Mass: {moles_to_grams(moles, molar_mass):.2f} g")
    elif choice == 2:
        grams = float(input("Enter grams: "))
        print(f"Moles: {grams_to_moles(grams, molar_mass):.2f} mol")
    elif choice == 3:
        mol = float(input("Enter moles: "))
        vol = float(input("Enter volume (L): "))
        print(f"Molarity: {calculate_molarity(mol, vol):.2f} M")
    elif choice == 4:
        mol = float(input("Enter moles: "))
        kg = float(input("Enter mass (kg): "))
        print(f"Molality: {calculate_molality(mol, kg):.2f} mol/kg")
    elif choice == 5:
        mass = float(input("Enter solute mass (g): "))
        vol = float(input("Enter volume (L): "))
        print(f"Normality: {calculate_normality(_
