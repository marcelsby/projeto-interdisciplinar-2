# Marcel Barbosa 2º TADS IFG JATAÍ
import sys

print('*** CALCULADORA DE MÉDIA ESCOLAR ***')

nota1 = float(input('Digite a primeira nota: '))

if nota1 < 0 or nota1 > 10:
  print('Nota inválida digitada!')
  print('\nSaindo...')
  exit()

nota2 = float(input('Digite a segunda nota: '))

if nota2 < 0 or nota2 > 10:
  print('Nota inválida digitada!')
  print('\nSaindo...')
  exit()

media = (nota1 + nota2) / 2

if media == 10:
  print(f'Média: {media} | Aprovado com Distinção!')
elif media >= 7:
  print(f'Média: {media} | Aprovado!')
elif media < 7:
  print(f'Média: {media} | Reprovado!')

print('\nSaindo...')
