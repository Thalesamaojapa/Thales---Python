#monte um programa que leia um numero e mostre o seu dobro, trilo e raiz quadrada

n = int(input('Digite um número inteiro '))
print('O dobro de {} é {} \nO triplo é {} \nE a raiz quadrada é {:.2f}'.format(n, n*2, n*3, (n**(1/2))))