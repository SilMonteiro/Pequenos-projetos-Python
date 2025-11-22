import random
lista = [1,2,3,4,5,6,7,8,9,10]
escolhido = random.choice(lista)
num = int(input('Digite um número entre 1 e 10: '))
while escolhido != num:
    print('Você errou, tente novamente! Digite o seu palpite: ')
print('Parabéns, vocÊ acertou!')
