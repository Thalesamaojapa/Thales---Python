#crie um conversor de celsius para fahrenheit

c = float(input('Digite aqui sua temperatura em Celsius: °C:'))
f = 9 * c / 5 + 32 
print('{}°C = {:.2f}°F'.format(c, f))