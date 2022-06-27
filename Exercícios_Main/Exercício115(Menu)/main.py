from módulos import clear, escreverArquivo, l, leiaInt, lerArquivo, título, leiaNome, deletarcadastros
from time import sleep

lendoarquivo = 0
arquivo = open('C:/Users/Thales/Desktop/Programação/Thales - Python/CursoEmVídeoPython/Exercício115(Menu)//cadastros.txt', 'r')
for linha in arquivo.readlines():
    lendoarquivo += 1
arquivo.close

cores = {    #cores normais

         'vermelho':'\033[31m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'branco':'\033[30m',
         'verde claro':'\033[91m',
         'verde':'\033[32m',
         'ciano':'\033[36m',
         'limpa':'\033[m',
         'preto e branco':'\033[7;97;m',

                #cores em negrito

         'vermelho em negrito':'\033[1;31m',
         'azul em negrito':'\033[1;34m' ,
         'amarelo em negrito':'\033[1;33m' ,
         'branco em negrito':'\033[1;97m',
         'roxo em negrito':'\033[1;35m',
         'verde em negrito':'\033[1;32m',
         'ciano em negrito':'\033[1;36m',

               #cores sublinhadas

         'vermelho sublinhado':'\033[4;31m',
         'azul sublinhado':'\033[4;34m',
         'amarelo sublinhado':'\033[4;33m',
         'branco sublinhado':'\033[4;97m',
         'roxo sublinhado':'\033[4;35m',
         'verde sublinhado':'\033[4;32m',
         'ciano sublinhado':'\033[4;36m'
         }


while True:
    sleep(1)
    clear() 
    título('MENU PRINCIPAL')
    print(f"""{cores["verde em negrito"]}1{cores["limpa"]} - {cores["azul"]}""", end=''
    f"""Ver pessoas cadastradas{cores["limpa"]}""")
    print(f"""\n{cores["verde em negrito"]}2{cores["limpa"]} - {cores["azul"]}""", end=''
    f"""Cadastrar nova pessoa{cores["limpa"]}""")
    print(f"""\n{cores["verde em negrito"]}3{cores["limpa"]} - {cores["azul"]}""", end=''
    f"""Sair do programa{cores["limpa"]}\n""")
    l()
    opção = leiaInt(f'{cores["verde em negrito"]}Sua opção: {cores["limpa"]}')
    if opção < 0 or opção > 3:
        while True:
            print(f'{cores["vermelho em negrito"]}ERRO! Opção ivnálida, escolha apenas opções listadas no menu.{cores["vermelho em negrito"]}')
            opção = leiaInt(f'{cores["verde em negrito"]}Sua opção: {cores["limpa"]}')
            if opção > 0 and opção < 3:
                break
    if opção == 1:
        clear()
        título('OPÇÃO 1')
        sleep(1)
        lerArquivo()
        l()
        sleep(1)
        if lendoarquivo > 0:
            print(f"""{cores["verde em negrito"]}1{cores["limpa"]} - {cores["azul"]}""", end=''
            f"""Voltar ao menu principal{cores["limpa"]}\n""")
            print(f"""{cores["verde em negrito"]}2{cores["limpa"]} - {cores["azul"]}""", end=''
            f"""Deletar algum cadastro{cores["limpa"]}\n""")
            print(f"""{cores["verde em negrito"]}3{cores["limpa"]} - {cores["azul"]}""", end=''
            f"""Modificar algum cadastro - Não funciona ainda{cores["limpa"]}\n""")
            while True:
                option = leiaInt(f'{cores["verde em negrito"]}Sua opção: {cores["limpa"]}')
                if option != 1 and option != 2 and option != 3:
                    print(f'{cores["vermelho em negrito"]}ERRO! Opção ivnálida, escolha apenas opções listadas no menu.{cores["vermelho em negrito"]}')
                else:
                    break
            if option == 2:
                clear()
                lerArquivo()
                l()
                print(f'{cores["verde em negrito"]}Digite o código do cadastro que deseja excluir. \nCaso deseja excluir todo cadastro digite "0"\n{cores["limpa"]}')
                while True:
                    opt = leiaInt(f'{cores["verde em negrito"]}Sua opção: {cores["limpa"]}')
                    if opt > lendoarquivo:
                        print(f'{cores["vermelho em negrito"]}ERRO! Por favor digite um código existente.{cores["limpa"]}')  
                    else:
                        break
                if opt == 0:
                    while True:
                        certeza = input(f'{cores["vermelho em negrito"]}Tem certeza que deseja exluir todos os cadastros? [S/N] {cores["limpa"]}').strip().upper()[0]
                        if certeza != 'N' and certeza != 'S':
                            print(f'{cores["vermelho em negrito"]}ERRO! Digite apenas S ou N! {cores["limpa"]}')
                        else:
                            break
                    if certeza == 'S':
                        l()
                        print(f'{cores["amarelo em negrito"]}Deletando cadastros...{cores["limpa"]}')
                        deletarcadastros()
                        sleep(1)
                        print('Cadastros deletados! Voltando para o menu...')
                        sleep(1)
                    else:
                        print('Voltando para o menu...')
                        sleep(1)
    if opção == 2:
        clear()
        título('OPÇÃO 2')
        sleep(1.5)
        while True:
            while True:
                a = leiaNome('Nome completo: ')
                b = leiaInt('Idade: ')
                certeza = input(f'{cores["verde em negrito"]}Tem certeza que deseja concluir o cadastro? [S/N]: {cores["limpa"]}').strip().upper()[0]
                if certeza != 'N' and certeza != 'S':
                    while True:
                        print(f'{cores["vermelho em negrito"]}ERRO! Digite apenas S ou N!{cores["limpa"]}')
                        certeza = input(f'{cores["verde em negrito"]}Tem certeza que deseja concluir o cadastro? [S/N]: {cores["limpa"]}').strip().upper()[0]
                        if certeza in 'SN':
                            break
                if certeza == 'S':
                    print(f'{cores["amarelo em negrito"]}Cadastrando nova pessoa...{cores["limpa"]}')
                    escreverArquivo(a, b)
                    sleep(1.5)
                    print(f'{cores["roxo em negrito"]}Cadastro concluído!{cores["limpa"]}')
                    sleep(2)
                    break
                if certeza == 'N':
                    print(f'{cores["vermelho em negrito"]}Cancelando cadastro...{cores["limpa"]}')
                    sleep(2)
                    break
            clear()
            continuar = input(f'{cores["verde em negrito"]}Deseja cadastrar outra pessoa? [S/N]: {cores["limpa"]}').strip().upper()[0]
            if continuar != 'N' and continuar != 'S':
                while True:
                    print(f'{cores["vermelho em negrito"]}ERRO! Digite apenas S ou N!{cores["limpa"]}')
                    continuar = input(f'{cores["verde em negrito"]}Deseja cadastrar outra pessoa? [S/N]: {cores["limpa"]}').strip().upper()[0]
                    if continuar in 'SN':
                        clear()
                        break
            if continuar == 'N':
                print(f'{cores["amarelo em negrito"]}Voltando ao menu...{cores["limpa"]}')
                sleep(2)
                clear()
                break
    if opção == 3:
        título('SAINDO DO PROGRAMA...')
        sleep(1.5)
        clear()
        break

    