# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas informações possiveis

palavra = input('Digite algo: ')
print('O tipo primitivo da sua palavra é:', type(palavra))
print('Seu dígito é número?', palavra.isnumeric())
print('Seu dígito é alfabético?', palavra.isalpha())
print('Seu dígito é alfanumérico?', palavra.isalnum())
print('Você não digitou nada, apenas um espaço?', palavra.isspace())
print('Sua palavra está em MAIÚSCULO?', palavra.isupper())
print('Sua palavra entá em minúsculo?', palavra.islower())

