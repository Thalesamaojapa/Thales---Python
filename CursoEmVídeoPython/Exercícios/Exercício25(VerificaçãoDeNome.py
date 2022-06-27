#faça um programa que verifique se começa ''santo'' no nome de uma cidade


cidade = str(input('Digite o nome da sua cidade: ')).strip()
print('Sua cidade começa com Santo? {}'.format(cidade[:5].lower() == 'santo'))