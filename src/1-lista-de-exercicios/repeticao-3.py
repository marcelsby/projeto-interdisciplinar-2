# Marcel Barbosa 2º TADS IFG JATAÍ
print('*** CADASTRO DO GOVERNO  ***')

a = 1

while a == 1:
    name = str(input('Digite seu nome (mais que 3 caracteres): '))

    if len(name) > 3:
        print('Nome OK!')
        a += 1
    else:
        print('Digite um nome válido!')

a = 2

while a == 2:
    age = int(input('Digite sua idade (entre 0 e 150): '))
    
    if age <= 150 and age >= 0:
        print('Idade OK!')
        a += 1
    else:
        print('Digite uma idade válida!')

a = 3

while a == 3:
    wage = float(input('Digite seu salário (maior que 0): '))

    if wage > 0:
        print('Salário OK!')
        a += 1
    else:
        print('Digite um salário válido!')

a = 4

while a == 4:
    gender = str(input('Digite seu gênero (M ou F): '))

    if gender == 'M' or gender == 'F':
        print('Gênero OK!')
        a += 1
    else:
        print('Digite um gênero válido!')

a = 5

while a == 5:
    civilState = str(input('Digite a inicial maiúscula do seu Estado Civíl (Solteiro(a), Casado(a), Viúvo(a), Divorciado(a)): '))
    if civilState == 'S' or civilState == 'C' or civilState == 'V' or civilState == 'D':
        print('Estado Civíl OK!')
        a +=1
    else:
        print('Digite uma inicial de um Estado Civíl válida!')

print(f'\n### Suas informações ###\nNome: {name}\nIdade: {age}\nSalário: {wage}\nGênero: {gender}\nEstado Civíl: {civilState}')

print('\nSaindo...')
