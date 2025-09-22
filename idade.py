def idade():
    ano_atual = int(input('Digite o ano de atual: '))
    ano_nasc = int(input('Digite o ano de nascimento: '))
    resultado = ano_atual - ano_nasc
    if resultado > 0:
        print(f'você tem {resultado} anos')
    else:
        print('Idade inválida')

idade()    