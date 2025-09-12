notas = []

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

notas.extend([nota1, nota2, nota3])
soma = sum(notas)
media = soma / len(notas)

if media >= 7:
    print('passou de ano!')
else: 
    print('recuperação!')