from flask import Flask, render_template, request, session
from chemcalc.core import (
    calculate_molar_mass, grams_to_moles, moles_to_grams,
    calculate_molarity, calculate_molality, calculate_normality,
    calculate_percent_yield, calculate_dilution, balance_equation
)

app = Flask(__name__)
app.secret_key = 'replace_this_secret_key_later'

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        calc_type = request.form.get('calc_type')
        try:
            session['use_count'] = session.get('use_count', 0) + 1
            if session['use_count'] > 6:
                return render_template('limit.html')

            if calc_type == 'moles_to_grams':
                moles = float(request.form['moles'])
                mm = float(request.form['molar_mass'])
                result = f"Result: {moles_to_grams(moles, mm):.2f} grams"

            elif calc_type == 'grams_to_moles':
                grams = float(request.form['grams'])
                mm = float(request.form['molar_mass'])
                result = f"Result: {grams_to_moles(grams, mm):.2f} moles"

            elif calc_type == 'molarity':
                mol = float(request.form['mol'])
                vol = float(request.form['vol'])
                result = f"Result: {calculate_molarity(mol, vol):.2f} M"

            elif calc_type == 'molality':
                mol = float(request.form['mol'])
                mass = float(request.form['mass'])
                result = f"Result: {calculate_molality(mol, mass):.2f} mol/kg"

            elif calc_type == 'normality':
                mass = float(request.form['mass'])
                eq = float(request.form['eq'])
                vol = float(request.form['vol'])
                result = f"Result: {calculate_normality(mass, eq, vol):.2f} N"

            elif calc_type == 'percent_yield':
                actual = float(request.form['actual'])
                theoretical = float(request.form['theoretical'])
                result = f"Result: {calculate_percent_yield(actual, theoretical):.2f}%"

            elif calc_type == 'dilution':
                c1 = float(request.form['c1'])
                v1 = float(request.form['v1'])
                c2 = float(request.form['c2'])
                result = f"Final volume (V2): {calculate_dilution(c1, v1, c2):.2f} L"

            elif calc_type == 'balance':
                reaction = request.form['reaction']
                result = balance_equation(reaction)

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
