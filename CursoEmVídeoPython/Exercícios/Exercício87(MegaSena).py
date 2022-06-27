from random import randint
lista = list()
Num_Jogos = int(input('Quantos jogos quer que eu sorteie? '))
for c in range(0, Num_Jogos):
    for jogo in range(0,6):
        if jogo == 0:
            lista.append(randint(0, 60))   
        else:
            num = randint(0, 60)
            if num not in lista:
                lista.append(num)
    print(f'Jogo {c + 1}: {sorted(lista)}')
    lista.clear()
