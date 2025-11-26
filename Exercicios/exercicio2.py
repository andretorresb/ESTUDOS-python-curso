##Exercício 2 – Média de notas com situação do aluno

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    situação = 'Aprovado'
elif 5 <= media < 7:
    situação = 'Recuperação'
else:
    situação = 'Reprovado'

print(f'A média do aluno é {media:.2f} situação: {situação}')