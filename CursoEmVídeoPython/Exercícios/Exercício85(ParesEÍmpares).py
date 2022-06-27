num = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º número: '))
    if n % 2 == 0:
        num[1].append(n)
    else:
        num[0].append(n)
num[0].sort()
num[1].sort()
print(f'Os números ímpares são: {num[0]}')
print(f'Os número pares são: {num[1]}')