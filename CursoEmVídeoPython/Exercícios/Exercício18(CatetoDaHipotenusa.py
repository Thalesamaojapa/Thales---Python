from math import sqrt, pow, ceil, floor,  
#faça um programa que leia os catetos e dê a hipotenusa

c1 = float(input('Coloque aqui o comprimento do cateto oposto: '))
c2 = float(input('Coloque aqui o comprimento do cateto adjacente '))
hipoqua = pow(c1, 2) + pow(c2, 2)
hipo = sqrt(hipoqua)
print('O comprimento da hipotenusa é = {}'.format(hipo))
print('Arredondado para cima: {}'.format(ceil(hipo)))
print('Arredondado para baixo: {}'.format(floor(hipo)))