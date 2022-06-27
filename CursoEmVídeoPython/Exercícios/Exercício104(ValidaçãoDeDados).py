def leiaInt(num):
    while True:
        n = input(num)
        if n.isnumeric():
            return n
        else:
            print('\033[31mERRO! Digite um número válido\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')