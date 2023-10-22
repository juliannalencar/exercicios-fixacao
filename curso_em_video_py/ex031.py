'''
Desenvolva um programa que pergunte a distância de uma viagem em KM. 
Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM, e R$0,45 para viagens mais longas.

'''

distancia = float(input('Digite a distância do trecho: '))

if distancia <= 200:
    print(distancia * 0.5)
else:
    print(distancia * 0.45)