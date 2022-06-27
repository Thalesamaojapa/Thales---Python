while True:
    posicao = int(input('Digite um número de 0 a 20: '))
    num = ('zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze',
    'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')  
    if posicao > 20 or posicao < 0:
        print('Você digitou um número fora dos pedidos. Tente novamente')
    else:
        print(f'Você digitou {num[posicao]}')
        break
