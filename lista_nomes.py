nomes = []

while True:
    nome = input("Digite o nome do voluntário (ou 'sair' para encerrar): ")
    nome.lower()

    if nome == "sair":
        print(nomes)
        break
    else:
        nomes.append(nome)

