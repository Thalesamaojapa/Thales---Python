expressão = input('Digite sua expressão aqui: ')
pilha = []
for simbolo in expressão:
    if simbolo == '(':
        pilha.append(simbolo)
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua experssão está certa!')
else:
    print('Sua expressão está errada...')
