valores = []

orcamento = float(input('Digite seu orçamento: R$'))

alimentacao = float(input('Digite quanto gastou com alimentação: R$'))
contas = float(input('Digite quanto gastou com contas: R$'))
lazer = float(input('digite quanto gastou com lazer: R$'))

valores.extend([alimentacao, contas, lazer])
total = sum(valores)

if total < orcamento:
    print('Você gastou menos do que seu orçamento, parabéns!')
else:
    print('Atenção, você ultrapassou o limite do orçamento!')

