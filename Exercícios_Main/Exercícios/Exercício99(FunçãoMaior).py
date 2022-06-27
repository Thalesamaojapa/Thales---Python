from time import sleep


def l():
    print('=-' * 15)    


def receber(*num):
    cont = maior = 0
    l()
    print('Analisando os valores passados...')
    for c, v in enumerate(num):
        if c == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        print(f'{v}', end=' ', flush=True)        
        cont += 1
    print(f'Ao todo foram informados {cont} valores.')
    print(f'O maior valor informado foi {maior}')
    sleep(2)


receber(2, 9, 4, 5, 7, 1)
receber(4, 7, 0)
receber(1,2)
receber(6)
receber()