def saudacao():
    hora = int(input('Digite a hora atual (0-23): '))
    if hora >= 0 and hora < 12:
        print('Bom dia!')
    elif hora >= 12 and hora <= 18:
        print('Boa tarde!')
    elif hora > 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Horário inválido!')

saudacao()