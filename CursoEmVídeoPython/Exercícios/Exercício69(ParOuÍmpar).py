from random import paretovariate, randint
vit = 0
print('=-' * 20)
print('Vamos jogar par ou ímpar!')
print('=-' * 20)
while True:
    num = int(input('Digite um valor: '))
    escolha = input('Par ou Ímpar? [P/1]: ').strip().upper()
    win = randint(1, 10)
    soma = win + num
    if escolha == 'P' and soma % 2 == 0:
        vit += 1
        print(f'Parabéns! Você escolheu {num} e o computador {win}. A soma é {soma}, um número par')
    elif escolha == 'I' and soma % 3 ==0:
        vit += 1
        print(f'Parabéns! Você escolheu {num} e o computador {win}. A soma é {soma}, um número ímpar')
    else:
        if vit <1:
            print('Você perdeu e não ganhou nenhuma vez :(')
        elif vit == 1:
            print('Você perdeu, mas ganhou 1 vez! \nParabéns!')
        else:
            print(f'Você perdeu, mas ganhou {vit} vezes! \nParabéns!')
        break
        

    