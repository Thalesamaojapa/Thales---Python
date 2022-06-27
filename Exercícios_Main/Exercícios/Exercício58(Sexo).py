sexo = input('Qual seu sexo? [M/F]:').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Sexo inválido. Tente novamente!:[M/F] ').strip().upper()[0]
print(f'Seu sexo, {sexo} foi validado com sucesso')