
from datetime import date
ano = date.today().year
contmaior = 0
contmenor = 0
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {} pessoa: '.format(c)))
    if ano - nasc == 18 or ano - nasc >= 18:
        contmaior = contmaior + 1
    else:
        contmenor = contmenor+  1
print('Das datas inseridas, {} pessoas são de menor e {} são de maior'.format(contmenor, contmaior))
