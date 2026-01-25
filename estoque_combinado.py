import sys

estoque1 = tuple(input("Produtos do estoque 1 (separados por vírgula): ").split(", "))
estoque2 = tuple(input("Produtos do estoque 2 (separados por vírgula): ").split(", "))

while True:
    resposta = input("Deseja juntar os itens dos dois estoques? (Responda 'Sim' para juntar ou 'sair' para encerrar o programa): ")
    resposta.lower()
    if resposta == "sim":
        estoque_combinado = estoque1 + estoque2
        print(estoque_combinado)
        break
    elif resposta == "sair":
        sys.exit("Encerrando programa...")
        break
    else:
        print("resposta inválida, tente novamente...")
