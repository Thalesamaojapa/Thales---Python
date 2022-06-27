listagem = ('lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
            'estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
            'mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)
cont = 0
for itens in listagem:
    if cont % 2 == 0:
        print(f'{itens:=<30}', end=' ')
    else:
        print(f'R${itens:.2f}')
    cont += 1

#SOLUÇÃO DO GUANABARA:
#listagem = ('lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
            #'estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
            #'mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)
#for pos in range(0, len(listagem)):
    #if pos % 2 == 0:
        #print(f'{listagem[pos]:.<30}', end='')   
    #else:
        #print(f'R${listagem[pos]:>10.2f}')
