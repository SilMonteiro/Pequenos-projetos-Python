#Aprovando empréstimo para comprar uma casa
valorcasa = float(input('Digite o valor da casa que deseja comprar: '))
salario = float(input('Digite o seu salário: '))
tempopagar = int(input('Por quantos anos você deseja financiar a casa? (Digite somente anos inteiros)'))
prestacao = valorcasa / (tempopagar * 12)
print(f'O valor de cada prestação será de R${prestacao:.2f}')
if prestacao >= salario * 0.3:
    print('Empréstimo negado! O valor da prestação ultrapassa o limite estipulado para o seu salário atual')
else:
    print('Parabéns! Empréstimo concedido com sucesso!')