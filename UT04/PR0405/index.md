# Practica 5 - Ejercicios con listas

### Ejercicios:

1.

```python

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

```

2.

```python

celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)

```

3.

```python

from functools import reduce

numeros = [1, 2, 3, 4, 5]
suma_acumulativa = reduce(lambda acc, x: acc + x, numeros)
print(suma_acumulativa)

```

4.

```python

palabras = ["perro", "gato", "elefante", "oso", "jirafa"]
palabras_largas = filter(lambda p: len(p) > 5, palabras)
palabras_largas_mayusculas = list(map(lambda p: p.upper(), palabras_largas))
print(palabras_largas_mayusculas)

```

5.

```python

from functools import reduce

numeros = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros)
producto_pares = reduce(lambda acc, x: acc * x, pares)
print(producto_pares)

```

6.

```python

from functools import reduce

numeros = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]
lista_plana = reduce(lambda acc, sublist: acc + sublist, numeros, [])
positivos = filter(lambda x: x > 0, lista_plana)
suma_positivos = reduce(lambda acc, x: acc + x, positivos)
print(suma_positivos)

```
