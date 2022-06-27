from datetime import date
Ano_atual = date.today().year
infos = dict()
infos['Nome'] = input('Nome: ')
Ano_nasc = int(input('Data de nascimento: '))
infos['Idade'] = Ano_atual - Ano_nasc
infos['Carteira'] = int(input('Carteira de trabalho (0 se não tiver): '))
if infos['Carteira'] != 0:
    infos['Contratação'] = int(input('Ano de contratação: '))
    infos['Salário'] = float(input('Salário: '))
    infos['Aposentadoria'] = infos['Contratação'] - Ano_nasc + 35
    for k, v in infos.items():
        if k == 'Salário':
            print(f'{k} tem o valor R${v:.2f}')
        else:
            print(f'{k} tem o valor {v}')
else:
    for k, v in infos.items():
        print(f'{k} tem o valor {v}')
