lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break
ímpar = lista[:]
par = lista[:]
for num in lista:
    if num % 2 == 0:
        ímpar.remove(num)
    elif num % 2 != 0:
        par.remove(num)
print(f'A lista completa de números é: {lista}')
print(f'Os números ímpares são: {ímpar}')
print(f'Os números pares são: {par}')
    