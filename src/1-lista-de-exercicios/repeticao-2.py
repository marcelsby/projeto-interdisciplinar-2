# Marcel Barbosa 2º TADS IFG JATAÍ
print('*** CADASTRO DE USUÁRIO ***')

i = 0

while i == 0:
  user = str(input('Insira um nome de usuário: '))
  passwd = str(input('Insira uma senha: '))

  if user == passwd:
    print('O usuário e a senha não podem ser iguais! Tente novamente.')
  else:
    print('Usuário cadastrado!')
    i += 1
