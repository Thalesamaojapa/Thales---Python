from random import choice
print('Vamos jogar pedra, papel ou tesoura!')
print('Escolha: \n \033[31m1: Para pedra \n \033[32m2: Para papel \n \033[34m3: Para tesoura\033[m')
continuar = 'S'
while continuar == 'S':
    escolha = int(input('Escolha: '))
    pedra = 'pedra'
    tesoura = 'tesoura'
    papel = 'papel'
    lista = [pedra, papel, tesoura]
    win = choice(lista)
    if escolha == 1 and win == tesoura:
        print('Parabéns! O computador escolheu {}... Você ganhou!'.format(win))
    elif escolha == 1 and win == papel:
        print('Ouch! O computador escolheu {}... Você perdeu! Tente novamente.'.format(win))
    elif escolha == 1  and win == pedra:
        print('Uau! Ambos escolheram pedra... Isso significa que ouve um empate!')
    elif escolha == 2 and win == papel:
        print('Uau! Ambos escolheram papel... Isso significa que ouve um empate!')
    elif escolha == 2 and win == pedra:
        print('Parabéns! O computador escolheu {}... Você ganhou!'.format(win))
    elif escolha == 2 and win == tesoura:
        print('Ouch! O computador escolheu {}... Você perdeu! Tente novamente.'.format(win))
    elif escolha == 3 and win == papel:
        print('Parabéns! O computador escolheu {}... Você ganhou!'.format(win))
    elif escolha == 3 and win == tesoura:
        print('Uau! Ambos escolheram tesoura... Isso significa que ouve um empate!')
    elif escolha == 3 and win == pedra:
        print('Ouch! O computador escolheu {}... Você perdeu! Tente novamente!'.format(win))
    elif escolha >= 3:
        print('Ei! Escolha entre 1 e 3! Não sabe ler não!?')
    continuar = str(input('Deseja jogar novamente? [S/N]: ')).strip().upper()

