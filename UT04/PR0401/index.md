# Practica 1 - El lenguaje de programación Python

### Ejercicios:

1.

```python

isNum = False
while isNum == False:
    num = input("Introduzca un numero: ")
    if num.isnumeric() == True:
        isNum = True

```

2.

```python

n = int(input("Ingrese numero: "))
k = int(input ("Ingrese cantidad de veces multiplicado: "))
i = 1
for i in range(int( k + 1)):
    print( n , " * " , i , " = " , n * i)
    i += 1

```

3.

```python

a = int(input("Introduzca un numero: "))
i = 1
for i in range(a + 1) :
    print("*" * i)
    i += 1

```

4.

```python

a = int(input("introduzca un numero: "))
for rank in range(1, a , 2):
    espacio = " "
    print(" " * (a - rank -1) , "*" * (2 * rank + 1))

```

5.

```python

numLow = int(input("Introduzca un numero: "))
numHigh = False
for a in range(4):
    num = int(input("Introduce numero: "))
    if num < int(numLow) :
        numLow = num
    elif num > int(numHigh):
        numHigh = num
print("El numero mayor es ", numHigh, ". Y el numero menor es ", numLow) 

```

6.

```python

cant = int(input("Introduzca cantidad: "))
uniActual = input("Introduzca la cantidad actual: ")
uniDeseada = input("Introduzca unidad deseada: ")
resul = 0

if uniActual == "milimetros" and uniDeseada == "centimetros":
    resul = cant*10
if uniActual == "milimetros" and uniDeseada == "metros":
    resul = cant*1000
if uniActual == "milimetros" and uniDeseada == "kilometros":
    resul = cant*1000000
if uniActual == "centimetros" and uniDeseada == "milimetros":
    resul = cant/10
if uniActual == "centimetros" and uniDeseada == "metros":
    resul = cant*100
if uniActual == "centimetros" and uniDeseada == "kilometros":
    resul = cant*100000
if uniActual == "metros" and uniDeseada == "milimetros":
    resul = cant/1000
if uniActual == "metros" and uniDeseada == "centimetros":
    resul = cant/100
if uniActual == "metros" and uniDeseada == "kilometros":
    resul = cant*1000
if uniActual == "kilometros" and uniDeseada == "milimetros":
    resul = cant/1000000
if uniActual == "kilometros" and uniDeseada == "centimetros":
    resul = cant/100000
if uniActual == "kilometros" and uniDeseada == "metros":
    resul = cant/1000
print(resul)

```

7.

```python

from random import *
num = randint(0,100)
ok = False
print (num)
while ok == False:
    i = int(input("Ingrese numero: "))
    if i == num:
        ok = True

```

8.

```python

mj1 = 0
mj2 = 0
while mj1 < 5 and mj2 < 5:
    j1 = input("Di la elección del jugador 1: ").lower()
    j2 = input("Di la elección del jugador 2: ").lower()

    match j1:
        case "piedra":
            if j2 in ["lagarto", "tijeras"]:
                res = "Gana jugador 1"
                mj1 += 1
            elif j2 in ["papel", "spok"]:
                res = "Gana jugador 2"
                mj2 += 1
            else:
                res = "Empate"

        case "papel":
            if j2 in ["piedra", "spok"]:
                res = "Gana jugador 1"
                mj1 += 1
            elif j2 in ["tijeras", "lagarto"]:
                res = "Gana jugador 2"
                mj2 += 1
            else:
                res = "Empate"

        case "tijeras":
            if j2 in ["papel", "lagarto"]:
                res = "Gana jugador 1"
                mj1 += 1
            elif j2 in ["piedra", "spok"]:
                res = "Gana jugador 2"
                mj2 += 1
            else:
                res = "Empate"

        case "lagarto":
            if j2 in ["spok", "papel"]:
                res = "Gana jugador 1"
                mj1 += 1
            elif j2 in ["tijeras", "piedra"]:
                res = "Gana jugador 2"
                mj2 += 1
            else:
                res = "Empate"

        case "spok":
            if j2 in ["tijeras", "piedra"]:
                res = "Gana jugador 1"
                mj1 += 1
            elif j2 in ["lagarto", "papel"]:
                res = "Gana jugador 2"
                mj2 += 1
            else:
                res = "Empate"

        case _:
            res = "Jugada no válida del jugador 1"

    print(res)
    print("Jugador 1:", mj1, "| Jugador 2:", mj2)

print("Jugador 1 gana la partida" if mj1 == 5 else "Jugador 2 gana la partida")

```

9.

```python

n = int(input("Ingrese un numero: "))
a = 0
b = 1
for i in range(n):
    print (a, " ")
    a, b = b, a + b

```

10.

```python

num = int(input("Introduce un numero: "))
primo = True
for i in range(2,num):
    if num % i == 0:
        primo = False
if primo == True:
    print("El numero es primo")
else:
    print("El numero no es primo")

```
