'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: 
    Digite um número: 1834

    unidade: 4
    dezena: 3
    centena: 8
    milhar 1

'''

numero = int(input('Digite um número entre 0 e 9999: '))
numero_separado = numero.strip()

print(f'Unidade: {numero[3]}')
print(f'Dezena: {numero[2]}')
print(f'Centena: {numero[1]}')
print(f'Milhar: {numero[0]}')