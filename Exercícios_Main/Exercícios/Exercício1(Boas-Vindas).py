#Criar um script Phyton que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o
#valor digitado

nome = input('Qual é o seu nome? ')
print('Bem-vindo ', nome)

#tentando fazer com .format que o reginho me ensinou
a = input('Qual é o seu nome?')
print('Bem-vindo {}'.format(a))

#usando 2 máscaras
a = input('Qual é o seu nome')  
b = input('Qual é o seu peso')
print('Seu nome é {} e seu peso {}'.format(a,b))
