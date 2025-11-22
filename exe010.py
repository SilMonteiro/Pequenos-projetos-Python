#Analisando valores
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor:'))
if v1 < v2:
    print('O segundo valor é maior!')
elif v2 < v1:
    print('O primeiro valor é maior!')
else:
    print('Não existe valor maior, os dois valores são iguais!')