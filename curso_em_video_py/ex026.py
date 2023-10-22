'''
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A";
- Em que posição ela aparece a primeira vez;
- Em que posição ela aparece a última vez.

'''

frase = str(input('Digite uma frase: ')).upper().strip()

quantidade_A = frase.count('A')
primeira_posicao = frase.find('A') + 1
ultima_posicao = frase.rfind('A') + 1

print(f'A letra "A" aparece {quantidade_A} vezes na frase.')
print(f'A primeira letra "A" apareceu na posição {primeira_posicao}.')
print(f'A última letra "A" apareceu na posição {ultima_posicao}.')



