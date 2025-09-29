a = int(input("introduzca un numero: "))
for rank in range(1, a , 2):
    espacio = " "
    print(" " * (a - rank -1) , "*" * (2 * rank + 1))
    