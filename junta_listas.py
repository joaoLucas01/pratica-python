produtos = input('Digite os produtos deparados por vírgula: ').split(',')
precos = input('Digite os preços dos produtos deparados por vírgula: ').split(',') 

for produto, preco in zip(produtos, precos):
    print(f'{produto.strip()}: {preco.strip()}')