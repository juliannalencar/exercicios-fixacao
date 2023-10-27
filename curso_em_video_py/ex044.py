# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de descorto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

valor_produto = float(input('Informe o valor do produto: '))

forma_pagamento = int(input('''Digite a forma de pagamento: 
      [ 1 ] Dinheiro ou Cheque
      [ 2 ] À vista no cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x no cartão: '''))

dinheiro = valor_produto * 0.1
cartao = valor_produto * 0.05
tres_vezes = valor_produto * 0.2

if forma_pagamento == 1:
    print(f'Você teve um desconto de R${dinheiro}, e pagará R${valor_produto - dinheiro}.')
elif forma_pagamento == 2:
    print(f'Você teve um desconto de R${cartao}, e paragrá R${valor_produto - cartao}.')
elif forma_pagamento == 3:
    print(f'A forma de pagamento escolhida não concede nenhum desconto ou acréscimo, e você paragá o valor de etiqueta R${valor_produto}.')
else:
    print(f'Você escolheu pagar o produto em 3x no cartão, e terá um acrescimo de R$ {tres_vezes}, e seu pagamento total será de {valor_produto + tres_vezes}.')

