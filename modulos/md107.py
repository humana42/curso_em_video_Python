def analise(valor):
    metade = dobro = au = 0
    metade = valor/2
    dobro = valor*2
    au = valor + (valor*0.1)
    print(f'A metade de R${valor} é R${metade:.2f}'.replace('.', ','))
    print(f'O dobro de R${valor} é R${dobro:.2f}'.replace('.', ','))
    print(f'O valor com aumento de 10% é R${au:.2f}'.replace('.', ','))