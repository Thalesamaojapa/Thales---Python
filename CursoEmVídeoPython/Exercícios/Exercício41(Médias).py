nota1 = float(input('Digite aqui a primeira nota: '))
nota2 = float(input('Digite aqui a segunda nota: '))
média = (nota2 + nota1) / 2
if média <= 5.0:
    print('Você foi \033[1;31mREPROVADO\033[m! Estude mais!')
elif média >= 5.0 and média <= 6.9:
    print('Você está de \033[1;33mRECUPERAÇÃO\033[m! Estude para a prova no final do ano!')
elif média >= 7.0:
    print('Você foi \033[1;32mAPROVADO\033[m! Parabéns!')