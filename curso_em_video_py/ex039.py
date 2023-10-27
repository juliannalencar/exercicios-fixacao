# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
idade = ano_atual - ano_nascimento

if idade < 18:
    print('Você ainda vai se alistar!')
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    print('Você já passou da hora de se alistar!')