hora_atual = int(input('Digite a hora atual (formato 24 horas)'))

if hora_atual > 8 and hora_atual < 18:
    print('acesso liberdo')
elif hora_atual < 8 or hora_atual > 18 :
    print('acesso negado')
elif hora_atual < 0 or hora_atual > 23: 
    print('horário inválido')