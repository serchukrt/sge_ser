from random import *
num = randint(0,100)
ok = False
print (num)
while ok == False:
    i = int(input("Ingrese numero: "))
    if i == num:
        ok = True
    