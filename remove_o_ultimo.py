pedidos = []

lista = input("Digite os itens separados por vírgula: ")

pedidos = [item.strip() for item in lista.split(",")]
pedidos.pop()
print(pedidos)
