# Marcel Barbosa 2º TADS IFG JATAÍ
print('*** PROGRAMA IDENTIFICADOR DE GÊNERO ***')

gender = str(input('Digite a sigla do gênero que deseja verificar: '))

if gender == 'F':
  print('A sigla digitada corresponde ao gênero FEMININO.')
elif gender == 'M':
  print('A sigla digitada corresponde ao gênero MASCULINO.')
else:
  print('Gênero inválido!')

print('\nSaindo...')
