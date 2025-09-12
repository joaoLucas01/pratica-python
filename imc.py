peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/ (altura * altura)
print(f'seu imc é {imc}')

if imc < 18.5:
    print('bateu um ventinho já voa')
elif imc < 25:
    print('beleza cara')
else:
    print('Tá gordinho')
