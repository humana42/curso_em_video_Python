def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrda = input(msg).replace(',','.').strip()
        if entrda.isalpha() or entrda == '':
            print(f'\033[0;31mERRO: \"{entrda}\" é um preço invalido!\033[m')
        else:
            valido = True
            return float(entrda)