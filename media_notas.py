notas = input("Digite as notas dos alunos separadas por viígula: ").split(", ")
notas = [float(nota) for nota in notas]
media = sum(notas) / len(notas)
if media > 7:
    print(f"A media da turma foi {media}, a turma está de parabens")
else:
    print(f"A media da turma foi {media}, a turma precisa melhorar")