nome = str(input('Qual é o seu nome? ')).strip()
print('No seu nome, a letra A aparece {}'.format(nome.lower().count('a')))
print('A letra A aparece pela primeira vez na casa {}'.format(nome.lower().find('a') + 1))
print('A letra A aparece pela última vez na casa {}'.format(nome.lower().rfind('a') + 1))
# o +1 é pra facilitar o usuário pois é raro contarmos a casa 0
