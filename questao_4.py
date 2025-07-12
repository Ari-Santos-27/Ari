# faça uma lista que tenha 100 numeros aleatorios entre 0 a 100

import random

numeros_aleatorios = []

for i in range(100):
    numero = random.randint(0, 100)
    numeros_aleatorios.append(numero)

print(numeros_aleatorios)
