import sys

convidados = ['Ana', 'Pedro', 'Carlos']

while True:
    vai_adicionar = input("Quer adicionar um novo convidado a lista? (S/N)")
    vai_adicionar = vai_adicionar.lower()
    if vai_adicionar == "n":
        sys.exit("encerrando o programa...")
    elif vai_adicionar == "s":
        convidado_novo = input("Digite o nome do novo convidado: ")
        posicao = int(input("Digite a posição na qual deseja inserir o convidado: "))

        if posicao > len(convidados) + 1 or posicao < 1:
            print('posição inválida, tente novamente')
        else:
            convidados.insert(posicao - 1 ,convidado_novo)
            print(convidados)
            while True:
                pergunta = input("gostaria de inserir mais convidados? (S/N)")
                pergunta = pergunta.lower()
                if pergunta == 's':
                    break
                elif pergunta == 'n':
                    sys.exit("encerrando programa...")
                else:
                    print("resposta inválida, tente novamente")
    else:
        print("resposta inválida, tente novamente")
        
        
