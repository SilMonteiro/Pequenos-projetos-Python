#Analisando triângulos
l1 = float(input('Digite o lado 1: '))
l2 = float(input('Digite o lado 2: '))
l3 = float(input('Digite o lado 3: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 and l2 == l3 and l3 == l1:
        print('O triângulo é equilátero!')
    if l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('O triângulo é isósceles!')
    if l1 != l2 and l1 != l3 and l2 != l1:
        print('O triângulo é escaleno!')
else:
    print('Não é possível formar um triângulo com essas medidas para os lados')