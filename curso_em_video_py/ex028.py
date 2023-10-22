'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

'''

from random import randint

computador = randint(0, 5)
jogador = int(input('Em que número eu pensei? '))

if computador == jogador:
    print(f'Pensei em {computador}. Você venceu!')

else:
    print(f'Pensei em {computador}. Você perdeu!')


