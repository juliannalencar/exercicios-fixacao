# Crie um programa que faça o computador jogar Jokenpô com você

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
      [ 0 ] PEDRA
      [ 2 ] PAPEL
      [ 3 ] TESOURA''')

jogador = int(input('Qual a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador vence!')
    elif jogador == 2:
        print('Computador vence!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:
    if jogador == 0:
        print('Computador vence!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador vence!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:
    if jogador == 0:
        print('Jogador vence!')
    elif jogador == 1:
        print('Computador vence!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
