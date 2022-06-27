#crie um programa que leia um número Real e mostre apenas sua porção inteira
from math import trunc 
n = float(input('Insira aqui seu número '))
print('A porção interia do seu número é: {}'.format(trunc(n)))
