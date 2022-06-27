soma = somaterceira = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for l in range(0,3):
        matriz[c][l] = int(input(f'Digite um número para [{c}, {l}]: '))
for t in range(0, 3):
    somaterceira += matriz[t][2]
    for y in range(0,3):
        print(f'[{matriz[t][y]:^5}]', end='')
        if matriz[t][y] % 2 == 0:
            soma += matriz[t][y]
    print()
print('=-' * 30)
print(f'A soma dos valores pares da matriz é {soma}')
print(f'A soma dos valores da terceira coluna é: {somaterceira}')
matriz[1].sort()
print(f'O maior valor da segunda linha é {matriz[1][-1]}')





