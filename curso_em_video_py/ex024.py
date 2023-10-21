'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

'''

cidade = input('Digite o nome da cidade: ').strip().capitalize()

mensagem = [
    'A cidade não começa com o nome "Santo".', 
    'A cidade começa com o nome "Santo".'
]

print(mensagem[cidade.startswith('Santo')])