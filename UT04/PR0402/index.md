# Practica 2 - Ejercicios con cadenas

### Ejercicios:

1.

```python

palabra = input("Introduce palabra: ").lower
voc = 0
con = 0
for i in palabra :
    if i in ["a","e","i","o","u"]:
        voc += 1
    else:
        con += 1
print("La palabra tiene")
print(voc, " vocales")
print(con, " consonantes")

```

2.

```python

a = input("Ingrese palabra: ")
print (a[::-1])

```

3.

```python

a = input("Introduzca palindromo: ")
limpio = a.replace(" ", "").lower()
if limpio == limpio[::-1]:
    print("Si es un palindromo")
else:
    print("No es un palindromo")

```

4.

```python

a = input("Introduzca frase: ")
grup = a.split(" ")
print(len(grup)," palabras")

```

5.

```python

cadena = input("Ingrese cadena: ")
caracteresVistos = set()
nuevaCadena = ""
for caracter in cadena:
    if caracter not in caracteresVistos:
        nuevaCadena += caracter
        caracteresVistos.add(caracter)
print ("Cadena sin duplicados: ", nuevaCadena)

```

6.

```python

a = input("Introduce una cadena: ")
nuevaCadena = ""
for i in a:
    if i == i.upper():
        nuevaCadena += i.lower()
    else:
        nuevaCadena += i.upper()
print (nuevaCadena)

```

7.

```python

a = input("Escribe una cadena: ")
i = int(input("Escribe numero: "))
print((a[i:]) + (a[:i]))

```

8.

```python

a = input("Introrduce la primera palabra: ")
b = input("Introduce la segunda palabra: ")
if sorted(a) == sorted(b):
    print("Si, " , a, " y ", b, " son anagramas")
else:
    print("No, " , a, " y ", b, " no son anagramas")

```

10.

```python

print("hello world")

```

11.

```python

print("hello world")

```

12.

```python

print("hello world")

```

13.

```python

print("hello world")

```