#tabuada
num = int(input('Digite o número da tabuada que deseja: '))
calc = 0
for a in range(0, 10):
    calc = num * a+1
    print(f'{calc}')