from time import sleep


def l():
    print('=-' * 15)


def contar(a, b, c):
    l()
    print(f'Contagem de {a} a {b} de {c} em {c}')
    l()
    sleep(2.5)
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ',end='', flush=True)
            sleep(0.5)
            cont += c
        print('Fim!')
    elif a > b:
        cont = a
        while cont >= b:
            print(f'{cont} ',end='', flush=True)
            cont -= c
        print('Fim!')
    
contar(1, 10, 1)
contar(10, 0, 2)
print('Agora é sua vez de contar!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Pulos: '))
contar(a, b, c)
