from functools import reduce

numeros = [1, 2, 3, 4, 5]
suma_acumulativa = reduce(lambda acc, x: acc + x, numeros)
print(suma_acumulativa)