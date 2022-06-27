import random
tot = 0
win = random.randint(1, 10)
print('Vamos jogar um jogo de adivinha! \nSeu computador pensou em um número de 1 a 10.')
palpite = int(input('Digite seu palpite!: '))
while palpite != win:
    tot += 1
    if palpite < win:
        print('É maior... Tente novamente!')
    elif palpite > win:
        print('É menor... Tente novamente!')   
    palpite = int(input('Digite seu palpite: '))
print(f'Muito bem! Você acertou! Foram ao todo {tot} tentativas!')
    
