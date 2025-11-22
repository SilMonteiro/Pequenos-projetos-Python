#contagem regressiva
import time
n = int(input('Digite quantos segundos restam para a queima de fogos: '))
for n in range(n, 0, -1):
    print(f'{n}')
    time.sleep(1)

print('FOGOOSSSS!!!!')