def total_de_vendas():
    vendas = input('Digite os valores das vendas: ').split()
    total = sum(map(float, vendas))
    print(f'O total de vendas foi: {total}')

total_de_vendas()