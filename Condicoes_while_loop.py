## == while loop - Condições == ##

# Excelente para loops dependentes de uma condição.

# Publicar


valor = int(input("Digite o valor do seu produto em R$: "))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor do produto agora é R${valor}')
    break
