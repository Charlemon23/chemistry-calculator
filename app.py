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
        print(f"Normality: {calculate_normality(mass, molar_mass, vol):.2f} N")

    elif choice == 6:
        actual = float(input("Enter actual yield (g): "))
        theoretical = float(input("Enter theoretical yield (g): "))
        print(f"Percent Yield: {calculate_percent_yield(actual, theoretical):.2f}%")

    elif choice == 7:
        c1 = float(input("Enter initial concentration (C1): "))
        v1 = float(input("Enter initial volume (V1): "))
        c2 = float(input("Enter final concentration (C2): "))
        print(f"Final volume (V2): {calculate_dilution(c1, v1, c2):.2f} L")

    elif choice == 8:
        reaction = input("Enter reaction (e.g., H2 + O2 or H2 + O2 = H2O): ")
        print("Balanced:", balance_equation(reaction))

    else:
        print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
