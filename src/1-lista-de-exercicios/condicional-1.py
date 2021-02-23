# Marcel Barbosa 2º TADS IFG JATAÍ
print('### CALCULADORA DE MAIOR VALOR ###')

value1=int(input('Insira o primeiro valor: '))

value2=int(input('Insira o segundo valor: '))

if value1 == value2:
  value = value1
  print(f'Os dois números inseridos tem o mesmo valor: {value}')
elif value1 > value2:
  print(f'Dentre os dois números inseridos o maior é o primeiro: {value1}')
elif value2 > value1:
  print(f'Dentre os dois números inseridos o maior é o segundo: {value2}')
