# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER

from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - ano_nascimento

print(f'Sua idade em {ano_atual} é {idade}.')
print('Sua categoria é:')

if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JUNIOR')
elif idade > 19 and idade <= 25:
    print('SENIOR')
else:
    print('MASTER')
    