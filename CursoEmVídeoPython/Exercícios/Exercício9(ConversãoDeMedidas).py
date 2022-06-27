#escreva um programa que leia um valor em metros e o exiba em cm e mm

from typing import MutableMapping


metro = float(input('Insira uma distância em metros: ' ))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print('A medida quando convertida equivale a: \n{} Km \n{} Hm \n{} Dam \n{} M \n{} Dm \n{} Cm \n{} Mm'.format(km, hm, dam, metro, dm, cm, mm))
