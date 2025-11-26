#Exercício 1 – Par, ímpar e múltiplo de 5

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    tipo = 'par'
else:
    tipo = 'impar'

if numero % 5 == 0:
   multiplo = "multiplo de 5."
else: 
    multiplo = "não é multiplo de 5."

print(f'o número {numero} é {tipo} e {multiplo}')
#fim do código
