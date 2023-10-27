# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isóceles: dois lados iguais
# Escaleno: todos os lados diferentes


r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR TRIANGULO!')
    if r1 == r2 and r1 == r3:
        print('Trata-se de um triângulo EQUILÁTERO, em que todos os lados são iguais.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Trata-se de um triângulo ISÓCELES, que possui dois lados iguais.')
    else:
        print('Trata-se de um triângulo ESCALENO, onde todos os lados são diferentes.')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')