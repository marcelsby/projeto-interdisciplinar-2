# Marcel Barbosa 2º TADS IFG JATAÍ

yearsCounter = 0

countryA = 80000
countryB = 200000

def growCountryA(country):
    country += (country * 0.03)
    return country

def growCountryB(country):
    country += (country * 0.015)
    return country

while countryA <= countryB:
    countryA = growCountryA(countryA)
    countryB = growCountryB(countryB)
    
    yearsCounter += 1

print(f'{yearsCounter} anos.')