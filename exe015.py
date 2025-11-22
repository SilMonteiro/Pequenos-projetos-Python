#soma de impares multiplos de 3 entre 0 e 500
import time
n = 0
soma = 0
for n in range(0, 501):
    if n % 2 != 0 and n % 3 ==0:
        print(n)
        time.sleep(0.5)
        soma += n
print(f'A soma total desses números é {soma}')

