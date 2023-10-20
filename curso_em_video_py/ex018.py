from math import radians, sin, cos, tan

angulo = float(input('Informe o ângulo que deseja calcular: '))
seno_angulo = sin(radians(angulo))
cosseno_angulo = cos(radians(angulo))
tangente_angulo = tan(radians(angulo))

print(f'O angulo informado foi {angulo}, seu seno é {seno_angulo:.2f}, o cosseno é {cosseno_angulo:.2f}, e a tangente é {tangente_angulo:.2f}')

