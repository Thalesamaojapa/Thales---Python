pt = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
continuar = 10
num = pt
cont = 0
while continuar != 0:
    print(num, end= ' ➝  ')
    num = num + raz
    continuar = continuar - 1 
    cont = cont + 1
    if continuar == 0:
        print('pausa')
        continuar = int(input('Quantos termos você quer mostrar a mais?: '))
print(f'Progressão finalizada com {cont} termos')