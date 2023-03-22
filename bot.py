
import random

def numero_a():
    rand = random.randrange(1,9)
    return rand

verifica_jogada = {1: 1, 2: 2, 3: 1, 
                   4: 2, 5: 0, 6: 1, 
                   7: 2, 8: 0, 9: 1}

verifica = numero_a()
jogadas = verifica_jogada

if jogadas[verifica] != 0:
    print(f'ja jogaram na posição {verifica}')
    verifica = numero_a()
else:
    print(f'Joguei na posição {verifica}')
    jogada = 2