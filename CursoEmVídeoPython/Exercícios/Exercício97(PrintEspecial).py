def escreva(msg):
    tamanho = len(msg) + 6
    print('-' * tamanho)
    print(f'{msg:^{tamanho}}')
    print('-' * tamanho)


escreva('Thales')
escreva('Eu amo o Thales')
escreva('Thales e Dedé vão se casar')
