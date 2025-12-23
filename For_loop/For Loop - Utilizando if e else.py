#Terceira Aula for loop com Condicionais

compra_realizada = True

dados_compra = 'Compra Realizada com sucesso, no valor de R$ 30,00'

for enviar in range(3):
    if compra_realizada:
        print(dados_compra)
        print('Será enviado no email os dados')
        break

else:
    print('falha na compra')