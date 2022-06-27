velocidade = float(input('Qual a velocidade do seu carro? Km/h: '))
velocidadeexedente = velocidade - 80
multa = 7 * velocidadeexedente
if velocidade >= 80:
    print('Você passou do limite de velocidade e será multado pelo valor de: R${:.2f}'.format(multa))
else:
    print('Muito bem! Você está dirigindo seguramente, continue assim!')

