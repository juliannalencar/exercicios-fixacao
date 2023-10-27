# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite o seu peso em KG: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL.')
elif imc >= 25 and imc < 30:
    print('Você está com SOBREPESO.')
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MÓRBIDA!!!')
    