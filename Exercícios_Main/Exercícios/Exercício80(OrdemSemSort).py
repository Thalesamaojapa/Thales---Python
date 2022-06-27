lista = []
for c in range(0,5):
    num = int(input(f'Digite o {c + 1} número: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print(f'Adicionei {num} no final da lista')
    else:
        pos = 0 
        while pos < len(lista):
            if num < lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionei o número {num} na posição {pos}')
                break
            pos+= 1
print(f'Sua lista: {lista}')
    