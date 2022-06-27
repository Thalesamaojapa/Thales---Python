def leiaInt(msg):
    while True:
        try:
            entrada = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido!\033[m')
        except(KeyboardInterrupt):
            print('O usuário preferiu não informar esse número')
            return 0 
        else:
            return entrada


def leiaFloat(msg):
    while True:
        try:
            entrada = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número real válido!\033[m')
        except(KeyboardInterrupt):
            print('O usuário preferiu não informar esse número')
            return 0
        else:
            return entrada


n1 = leiaInt('Digite um número Inteiro: ')
n2 = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')




