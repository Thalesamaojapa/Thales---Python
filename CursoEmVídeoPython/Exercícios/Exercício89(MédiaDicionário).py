dados = dict()
dados['Nome'] = input('Nome do aluno: ')
dados['Média'] = float(input('Média do Aluno: '))
if dados['Média'] < 7:
    dados['Situação'] = 'Reprovado'
else:
    dados['Situação'] = 'Aprovado'
for k, v in dados.items():
    print(f'{k} é igual a {v}')