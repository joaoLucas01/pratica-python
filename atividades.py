A = int(input('informe os dias para a atividade A:'))
B = int(input('informe os dias para a atividade B:'))
C = int(input('informe os dias para a atividade C:'))

if A | B | C < 0:
    print('Os dias não podem ser negativos')
else:
    print('beleza cara')