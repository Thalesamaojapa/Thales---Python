pl = input('Digite uma frase: ').upper().split()
pljunt = ''.join(pl)
numdeletra = len(pljunt)
inverso = ''
for letra in range(numdeletra -1, -1, -1):
    inverso = inverso + pljunt[letra]     
if inverso == pljunt:
    print('{} ao contrário é {}, temos um palíndromo!'.format(pljunt, inverso))
else:
    print('{} ao contrário é {}'.format(pljunt, inverso))