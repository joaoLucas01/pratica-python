resultado = ["Ana", "Carlos", "Pedro"]
print(f"lista original: {resultado}")


erro = input("digite o nome do corredor que está errado: ")
erro = erro[0].upper() + erro[1:]
if erro in resultado:
    correto = input("digite o nome correto: ")
    posicao = resultado.index(erro)
    resultado.remove(erro)
    resultado.insert(posicao, correto)
    print(f"O nome {erro} foi substituído por {correto}")
    print(f"Lista atualizada: \n {resultado}")
else:
    print("nome não encontrado")