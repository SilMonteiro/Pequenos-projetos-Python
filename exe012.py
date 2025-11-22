#Pedra, papel ou tesoura
from random import choice
jogo = ['pedra', 'papel', 'tesoura']
jogador = str(input('Pedra, papel ou tesoura? '))
computador = choice(jogo)
print(f'Eu escolhi {computador}')

#empate
if jogador == 'pedra' and computador == 'pedra':
    print('Empate')
if jogador == 'tesoura' and computador == 'tesoura':
    print('Empate')
if jogador == 'papel' and computador == 'papel':
    print('Empate')

#outros
if jogador == 'pedra' and computador == 'tesoura':
    print('Você ganhou!')
if jogador == 'pedra' and computador == 'papel':
    print('Você perdeu!')
if jogador == 'tesoura' and computador == 'pedra':
        print('Você perdeu!')
if jogador == 'tesoura' and computador == 'papel':
        print('Você ganhou!')
if jogador == 'papel' and computador == 'tesoura':
    print('Você perdeu!')
if jogador == 'papel' and computador == 'pedra':
    print('Você ganhou!')
