def jogador(a='', b=''):
    a = input('Nome do jogador: ')
    b = str(input('Número de gols: '))
    teste = b.isnumeric()
    if teste == False:
        b = 0
    if a == '':
        a = '<desconhecido>'

    print(f'O jogador {a} fez {b} gol(s) no campeonato')


jogador()