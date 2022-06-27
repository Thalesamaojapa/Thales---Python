def leiaDinheiro(num):
    Válido = False
    while not Válido:
        entrada = str(input(num)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '' or entrada.isalnum():
            print(f'\033[31mERRO! {entrada} é um preço inválido!\033[m')
        else:
            Válido = True
            return float(entrada)
