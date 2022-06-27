from random import choice  
#um professor quer sortear um dos seus 4 alunos para apagar o quadro, crie um programa que ajude ele

n1 = str(input('Qual o nome do primeiro aluno? '))
n2 = str(input('Qual o nome do segundo aluno? '))
n3 = str(input('Qual o nome do terceiro aluno? '))
n4 = str(input('Qual o nome do quarto aluno? '))
#conceito novo!
lista = [n1, n2, n3, n4]
sorteado = choice(lista)
print('Parabéns! O ganhador foi: {}'.format(sorteado))
