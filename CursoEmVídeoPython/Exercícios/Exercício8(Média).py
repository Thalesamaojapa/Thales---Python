#faça um programa que leia 2 notas de um aluno, calcule e mostre sua média
nota1 = float(input('Insira aqui a primeira nota do aluno: '))
nota2 = float(input('Insira aqui a segunda nota do aluno: '))
média = (nota1 + nota2) / 2
print('Sua média é de {}'.format(média))
print('Sua média arredondada é: {:.0f}'.format(média))

