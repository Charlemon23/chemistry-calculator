from molmass import Formula
from chempy import balance_stoichiometry

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
    return sum(get_element_info(i) for i in range(num_elements))

def grams_to_moles(mass, molar_mass):
    return mass / molar_mass

def moles_to_grams(moles, molar_mass):
    return moles * molar_mass

def calculate_molarity(moles, volume):
    return moles / volume

def calculate_molality(moles, mass):
    return moles / mass

def calculate_normality(mass, equivalent_weight, volume):
    return (mass / equivalent_weight) / volume

def calculate_percent_yield(actual, theoretical):
    return (actual / theoretical) * 100

def calculate_dilution(c1, v1, c2):
    return (c1 * v1) / c2

def balance_equation(reaction):
    if '=' in reaction:
        reac_str, prod_str = reaction.split('=')
        reac = [r.strip() for r in reac_str.split('+')]
        prod = [p.strip() for p in prod_str.split('+')]
    else:
        reac = [r.strip() for r in reaction.split('+')]
        prod = []
        for r in reac:
            if 'C' in r and 'H' in r:
                prod += ['CO2', 'H2O']
            elif 'Na' in r and 'Cl' in r:
                prod += ['NaCl']
        prod = list(set(prod))
    reac_bal, prod_bal = balance_stoichiometry(reac, prod)
    reac_part = ' + '.join(f"{v} {k}" for k, v in reac_bal.items())
    prod_part = ' + '.join(f"{v} {k}" for k, v in prod_bal.items())
    return f"{reac_part} -> {prod_part}"
