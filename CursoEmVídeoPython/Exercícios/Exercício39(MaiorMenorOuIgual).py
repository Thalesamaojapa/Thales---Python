n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n1 == n2:
    print('Ambos os número são iguais!')
elif n1 >= n2 :
    print('{} é o maior número\n{} é o menor número!'.format(n1, n2))
elif n2 >= n1:
    print('{} é maior número!\n{} é menor número'.format(n2, n1))
