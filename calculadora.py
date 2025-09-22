soma = lambda x,y: x + y
subtracao = lambda x,y: x - y
multiplicacao = lambda x,y: x * y
divisao = lambda x,y: x / y

x = float(input('digite o primeiro número: '))
y = float(input('digite o segundo número: '))
operacao = input('digite a operação | + | - | * | / | : ')

if operacao == '+':
    print(f'o resultado da soma é: {soma(x,y)}')

elif operacao == '-':
    print(f'o resultado da subtração é: {subtracao(x,y)}')

elif operacao == '*':
    print(f'o resultado da multiplicação é: {multiplicacao(x,y)}')

elif operacao == '/':
    print(f'o resultado da divisão é: {divisao(x,y)}')


else:
    print('operação inválida')