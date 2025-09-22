usuario = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')

while len(usuario) < 5 or len(senha) < 8:
    if len(usuario) < 5:
        print('O nome de usuário deve ter pelo menos 5 caracteres')
    else:
        print('A senha deve ter pelo menos 8 caracteres')
    usuario = input('Digite seu nome de usuário:')
    senha = input('Digite sua senha')
print('Cadastro realizado com sucesso!')