n = int(input("Ingrese numero: "))
k = int(input ("Ingrese cantidad de veces multiplicado: "))
i = 1
for i in range(int( k + 1)):
    print( n , " * " , i , " = " , n * i)
    i += 1