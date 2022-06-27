import math
peso = float(input('Digite aqui seu peso: Kg: '))
altura = float(input('Digite aqui sua altura: m: '))
imc = peso / pow(altura, 2)
if imc <= 18.5:
    print('Você está abaixo do peso! Seu imc é {}'.format(imc))
elif imc == 18.5 or imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal! Seu imc é {}'.format(imc))
elif imc == 25 or imc >= 25 and imc <= 30:
    print('Você está com sobrepeso! Seu imc é {}'.format(imc))
elif imc == 30 or imc >= 30 and imc <= 40:
    print('Você está com obesidade! Seu imc é {}'.format(imc))
elif imc == 40 or imc >= 40:
    print('Você está com obesidade mórbida! Seu imc é {}'.format(imc))
    