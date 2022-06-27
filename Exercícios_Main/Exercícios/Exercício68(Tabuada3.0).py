while True:
    num = int(input('Digite um número para saber sua tabuada: '))
    if num <= 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c}')   
print('Programa finalizado com sucesso')
