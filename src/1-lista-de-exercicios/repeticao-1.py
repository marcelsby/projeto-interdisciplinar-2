# Marcel Barbosa 2º TADS IFG JATAÍ
print('*** CADASTRO DE NOTA ***')

i = 0

while i == 0:
  nota = float(input('Insira uma nota entre zero e dez: '))

  if nota < 0 or nota > 10:
    print('Nota inválida digitada!')
  else:
    print(f'Nota inserida: {nota}')
    i += 1
