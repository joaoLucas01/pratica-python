texto_1 = set(input(f"Texto 1: ").split(" "))
texto_2 = set(input(f"Texto 2: ").split(" "))

intersecao = texto_1.intersection(texto_2)
print(f"Palavras em comum: {intersecao}")