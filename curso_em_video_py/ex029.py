'''
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada km acima do limite.

'''

velocidade = float(input('Informe a velocidade do carro em Km: '))
limite_velocidade = 80

if velocidade > limite_velocidade:
    print(f'Você foi multado e paragá R${(velocidade - limite_velocidade) * 7} reais!')
else:
    print(f'Você não ultrapassou o limite de velocidade.')