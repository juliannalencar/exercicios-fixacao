'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas;
- O nome com todas minúsculas;
- Quantas letras ao todo (sem considerar espaços);
- Quantas letras tem o primeiro nome.

'''

nome = input('Digite seu nome completo: ')
nome_vazio = nome.replace(' ', '')
nome_lista = nome.split()

print(nome.upper())
print(nome.lower())
print(len(nome_vazio))
print(nome_lista[0])
