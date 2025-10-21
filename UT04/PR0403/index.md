# Practica 3 - Ejercicios con listas

### Ejercicios:
#### 1. Operaciones con listas

1.

```python

nombres.sort()
nombres.reverse()
print(nombres)

```

2.

```python

contador = sum(1 for nombre in nombres if nombre[0].upper() in ("A", "Á"))
print(contador)

```

3.

```python

nombre = input("Escribe un nombre: ").strip().capitalize()

if nombre in nombres:
    posicion = nombres.index(nombre)
    print("El nombre ", nombre, " esta en la posición", posicion)
else:
    print("El nombre introducido no se encuentra dentro de la lista")

```

4.

```python

nombre = input("Introduce tu nombre: ").strip().capitalize()

if nombre in nombres:
    posicion = nombres.index(nombre)
    anteriores = nombres[:posicion]
    print("Los nombres que están antes del tuyo son: ")
    print(", ".join(anteriores))
else:
    print("El nombre introducido no se encuentra dentro de la lista")

```

5.

```python

print("hello world")

```

6.

```python

print("hello world")

```

7.

```python

print("hello world")

```

8.

```python

print("hello world")

```

#### 2. Más ejercicios con listas

1.

```python

print("hello world")

```

2.

```python

print("hello world")

```

3.

```python

print("hello world")

```

4.

```python

print("hello world")

```

5.

```python

print("hello world")

```

6.

```python

print("hello world")

```

7.

```python

print("hello world")

```

8.

```python

print("hello world")

```

9.

```python

print("hello world")

```

10.

```python

print("hello world")

```