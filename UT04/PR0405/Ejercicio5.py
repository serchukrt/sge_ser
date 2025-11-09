from functools import reduce

numeros = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros)
producto_pares = reduce(lambda acc, x: acc * x, pares)
print(producto_pares)