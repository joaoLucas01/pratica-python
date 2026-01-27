palavra_chave = input("digite a palavra chave: ")
tamanho = len(palavra_chave)
primeiras = palavra_chave[:3]
ultimas = palavra_chave[tamanho-3:]
print(f"primeiras letras: {primeiras}")
print(f"últimas letras: {ultimas}")
