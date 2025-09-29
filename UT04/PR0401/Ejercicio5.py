numLow = int(input("Introduzca un numero: "))
numHigh = False
for a in range(4):
    num = int(input("Introduce numero: "))
    if num < int(numLow) :
        numLow = num
    elif num > int(numHigh):
        numHigh = num
print("El numero mayor es ", numHigh, ". Y el numero menor es ", numLow)     
    