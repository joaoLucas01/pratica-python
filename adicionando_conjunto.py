convidados = set()

while True:
    convidado = input("Digite o nome do convidado: ")
    convidado = convidado.lower()
    if convidado == "sair":
        print(convidados)
        break
    else:
        convidados.add(convidado)