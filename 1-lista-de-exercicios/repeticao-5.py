# Marcel Barbosa 2º TADS IFG JATAÍ

yearsCounter = 0

# Input e validação do primeiro país
validationCode = False

while validationCode == False:
    popCountryA = int(input('Digite a população do primeiro país: '))

    if type(popCountryA) == int:
        validationCode = True
    else:
        print('Digite uma quantidade populacional válida!')


validationCode = False

while validationCode == False:
    growTaxCountryA = float(input('Digite o percentual de taxa de crescimento populacional do primeiro país (formato decimal): '))

    if type(growTaxCountryA) == float and growTaxCountryA > 0:
        validationCode = True
    else:
        print('Digite uma taxa de crescimento populacional válida!')


# Input e validação do segundo país
validationCode = False

while validationCode == False:
    popCountryB = int(input('Digite a população do segundo país: '))

    if type(popCountryB) == int:
        validationCode = True
    else:
        print('Digite uma quantidade populacional válida!')


validationCode = False

while validationCode == False:
    growTaxCountryB = float(input('Digite o percentual de taxa de crescimento populacional do segundo país (formato decimal): '))

    if type(growTaxCountryB) == float and growTaxCountryB > 0:
        validationCode = True
    else:
        print('Digite uma taxa de crescimento populacional válida!')

# Output
def growCountryPopulation(countryPop, growTax):
    countryPop += (countryPop * growTax)
    return countryPop

if popCountryB > popCountryA:
    while popCountryA <= popCountryB:
        popCountryA = growCountryPopulation(popCountryA, growTaxCountryA)
        popCountryB = growCountryPopulation(popCountryB, growTaxCountryB)

        yearsCounter += 1
else:
    while popCountryA >= popCountryB:
        popCountryA = growCountryPopulation(popCountryA, growTaxCountryA)
        popCountryB = growCountryPopulation(popCountryB, growTaxCountryB)
        
        yearsCounter += 1

print(f'{yearsCounter} anos.')