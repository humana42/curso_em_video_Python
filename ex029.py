v = float(input('Qual a velocidade do carro? '))
if v>80:
    uv = v - 80
    uvv = uv * 7
    print('O carro utrapassou {:.2f}KM do limite de velocidade e recebeu uma multa de R${:.2f}'.format(uv, uvv))