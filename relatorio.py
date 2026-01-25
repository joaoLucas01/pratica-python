alunos = []
      
while True:
    iniciar = input("gostaria de cadastrar novo aluno? (S/N): ")
    iniciar = iniciar.lower()
    if iniciar == "s":
        cadastro = list(input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ").split(", "))
        nome, idade, nota = cadastro
        aluno = {
            "nome": nome, 
            "idade": idade, 
            "nota": nota
        }
        alunos.append(aluno)
        print(alunos)

    elif iniciar == "n":
        print(alunos)
        break
    else:
        print("resposta inválida, tente novamente...")