pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
for c in range(pt, pt + (11 - 1) * razao, razao):
    print(c)