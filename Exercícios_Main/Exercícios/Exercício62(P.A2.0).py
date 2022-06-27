pt = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
cont = pt
while cont != pt + (11 - 1) * raz:
    print(cont, end=' ➝  ')
    cont = cont + raz
print('Fim')