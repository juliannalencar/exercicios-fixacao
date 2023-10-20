import math

cateto_oposto = float(input('Digite o cateto oporto de um triângulo retângulo: '))
cateto_adjacente = float(input('Digite o cateto adjacente de um triângulo retângulo: '))
hipotenusa_quadrado = pow(cateto_oposto, 2) + pow(cateto_adjacente, 2)
hipotenusa = math.sqrt(hipotenusa_quadrado)

print('{:.2f}'.format(hipotenusa))