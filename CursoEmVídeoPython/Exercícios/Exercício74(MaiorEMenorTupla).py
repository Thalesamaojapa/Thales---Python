from random import randint

num = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
arrumado = sorted(num)
print(f'Sorteei os números: {num}')
print(f'O maior número é {arrumado[-1]}')
print(f'O menor número é {arrumado[0]}')


