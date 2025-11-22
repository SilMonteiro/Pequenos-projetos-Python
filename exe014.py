#numeros pares entre 1 e 50
import time
n = 50
for n in range(0, 51):
    if n % 2 == 0:
        print(f'{n}')
        time.sleep(0.5)
