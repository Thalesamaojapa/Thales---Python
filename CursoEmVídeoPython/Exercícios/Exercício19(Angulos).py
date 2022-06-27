#programa que leia o angulo e dê o seno, cosseno e tangente
from math import tan, cos, sin, radians

ang = float(input('Digite aqui o ângulo a ser analizado: '))

print('Seu seno é = {:.2f}'.format(sin(radians(ang))))
print('Seu cosseno é = {:.2f}'.format(cos(radians(ang))))
print('Sua tangente é = {:.2f}'.format(tan(radians((ang)))))
