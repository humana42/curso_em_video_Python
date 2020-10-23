n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m < 5:
    print('sua media foi de {:.1f} e está REPROVADO!'.format(m))
elif m > 5 and m < 6.9:
    print('sua media foi de {:.1f} e está de RECUPERAÇÃO!'.format(m))
elif m >= 7:
    print('sua media foi de {:.1f} e está APROVADO!'.format(m))
