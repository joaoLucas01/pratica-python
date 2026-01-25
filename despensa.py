despensa = ["pão de forma", "leite", "arroz", "feijão"]

item = input("Digite o item que você quer verificar: ")
if item in despensa:
    print(f"temos o item {item} na despensa")
else:
    print(f"o item {item} precisa ser comprado")