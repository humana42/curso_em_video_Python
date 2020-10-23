ex = input('Digite sua expressão: ')
paren = parenV = 0
for i, n in enumerate(ex):
   if n == '(':
       paren +=1
   elif n == ')':
       parenV += 1
if parenV == paren:
    print('Expressão valida')
else:
    print('Expressão invalida')
