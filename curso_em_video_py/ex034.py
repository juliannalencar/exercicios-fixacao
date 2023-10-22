'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

'''

salario = float(input('Digite seu salário: '))

if salario > 1250:
    print(f'Seu salário atual é R${salario} e vc receberá R${salario * 0.1} de aumento, totalizando o valor de R${salario + salario * 0.1}.')
else:
    print(f'Seu salário atual é R${salario} e vc receberá R${salario * 0.15} de aumento, totalizando o valor de R${salario + salario * 0.15}.')
