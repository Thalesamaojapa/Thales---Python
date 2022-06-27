from time import sleep
from os import system

def l():
    print('=-' * 18)


def título(msg):
    l()
    print(msg.center(30))
    l()


def escreverArquivo(nome, idade):
    arquivo = open('C:/Users/Thales/Desktop/Programação/Thales - Python/CursoEmVídeoPython/Exercício115(Menu)//cadastros.txt', 'a')
    arquivo.write(f'\n{nome};{idade}')
    arquivo.close()

def leiaInt(msg):
    while True:
        try:
            entrada = int(input(msg))
        except:
            print('\033[1;31mERRO! Por favor, digite um número válido!\033[m')
        else:
            return entrada


def lerArquivo():
    cont = 0
    tamanho = 0
    arquivo = open('C:/Users/Thales/Desktop/Programação/Thales - Python/CursoEmVídeoPython/Exercício115(Menu)//cadastros.txt', 'r')
    for linha in arquivo.readlines():
        if linha != '':
            if len(linha) > tamanho:
                tamanho = len(linha)
    if tamanho == 0:
        print('Nenhum cadastro existente')
    else:   
        print(f'{"Cód"} {"Nome":<{tamanho}}{"Idade"}')
        sleep(0.4)
        arquivo = open('C:/Users/Thales/Desktop/Programação/Thales - Python/CursoEmVídeoPython/Exercício115(Menu)//cadastros.txt', 'r')
        print('-' * 36)
        sleep(0.4)
        for cadastro in arquivo.readlines():
            
            try:
                linhasep = cadastro.split(';')
                print(f'{cont + 1} {linhasep[0]:<{tamanho + 3}} {linhasep[1]:>1}'.replace('\n', ''), flush=True)
                sleep(0.35)                         
            except:
                print(end='')  
                cont -= 1
            finally:
                cont += 1 

def leiaNome(msg):
    while True:
        entrada = input(msg).title()
        if entrada.isnumeric():
            print('\033[1;31mERRO! Por favor, digite um nome válido!\033[m')
        elif len(entrada.split(' ')) <= 1:
            print('\033[1;31mERRO! Por favor, digite o nome completo!\033[m')
        else:
            return entrada


def clear():
    _ = system('cls')


def deletarcadastros():
    arquivo = open('C:/Users/Thales/Desktop/Programação/Thales - Python/CursoEmVídeoPython/Exercício115(Menu)//cadastros.txt', 'w')
    arquivo.close()    





    
