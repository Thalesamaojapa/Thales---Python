def fatorial(num, show=False):
    cont = num
    fatorial = 1
    while cont != 0:
        if show == True:
            print(cont, end=' ')
            if cont != 1:
                print('x', end=' ')
            else:
                print('=')    
        fatorial *= cont
        cont -= 1
    return fatorial
print(fatorial(5, show=True))
 