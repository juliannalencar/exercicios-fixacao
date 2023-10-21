'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

'''

nome = input('Digite seu nome: ').upper()

mensagem = [
    f"Seu nome '{nome}' não tem 'SILVA'.", 
    f"Seu nome '{nome}' tem 'SILVA'."
]

print(mensagem['SILVA' in nome])