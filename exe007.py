velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade -80)*7
if velocidade > 80:
    print(f'Você ultrapassou o limite de velocidade e por isso deverá pagar uma multa de R${multa:.2f}')
