from time import sleep
num1 = float(input('\nPrimeiro valor: '))
num2 = float(input('Segundo valor: '))
opção = 0
while opção != 5:
    sleep(0.5)
    print('       [ 1 ] Somar')
    print('       [ 2 ] Multiplicar')
    print('       [ 3 ] Maior')
    print('       [ 4 ] Novos números')
    print('       [ 5 ] Sair do programa')
    opção = int(input('>>>>> Qual sua opção: '))
    sleep(0.5)
    if opção == 1:
        print(f'A soma entre {num1} e {num2} é {num1 + num2}')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    elif opção == 2:
        print(f'O produto entre {num1} e {num2} é {num1 * num2}')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    elif opção == 3:
        if num1 == num2:
            print('Os números são iguais, não há um maior')
        elif num2 >= num1:
            print(f'{num2} é maior que {num1}, logo ele é o maior número')
        elif num1 >= num2:
            print(f'{num1} é maior que {num2}, logo ele é o maior número')
            print('Os números são iguais, não há um maior')
    elif opção == 4:
        num1 = float(input('Digite o novo primeiro valor: '))
        num2 = float(input('Digite o novo segundo número: '))
    elif opção == 5:
        print('Finalizando o programa')
        sleep(2)
        print('Programa finalizado com sucesso!')
