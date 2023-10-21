'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
último = Souza

'''

nome_completo = input('Digite seu nome completo: ').title()

nome_separado = nome_completo.strip().split()

print('Primeiro nome: ', nome_separado[0])
print('Ultimo nome: ', nome_separado[-1])
