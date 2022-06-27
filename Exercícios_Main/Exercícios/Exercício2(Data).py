#Criar um script Python que leia dia, mês e o ano de nascimento de uma pessoa e uma mensagem com a data formatada

#primeiro usando ,
a = input ('Que dia você nasceu? ')
b = input ('Que mês você nasceu? ')
c = input ('Que ano você nasceu? ')
print (a,'/', b, '/', c)

#agr usando máscara
a = input ('Que dia você nasceu?')
b = input ('Que mês você nasceu?')
c = input ('Que ano você nasceu?')
print ('Você nasceu em {}/{}/{}'.format(a,b,c))


