#faça um programa que leia a altura e o largura de uma parede e de sua área e a quantidade de tinta
#necessária pra pintar sabendo que cada litro de tinta pinta uma área de 2m²

altura = float(input('Qual a altura da parede?: '))
largura = float(input('Qual a largura da parede?: '))
área = altura * largura
tinta = área / 2
print('A área da parede é de {:.2f}m²'.format(área))
print('Considerando que cada litro de tinta pinta uma área de 2m², seriam necessários aproximadamente {:.0f} litros de tinta para pintar toda \na parede'.format(tinta))
