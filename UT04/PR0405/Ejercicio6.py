from functools import reduce

numeros = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]
lista_plana = reduce(lambda acc, sublist: acc + sublist, numeros, [])
positivos = filter(lambda x: x > 0, lista_plana)
suma_positivos = reduce(lambda acc, x: acc + x, positivos)
print(suma_positivos)