num = int(input("Introduce un numero: "))
 
primo = True
 
for i in range(2,num):
    if num % i == 0:
        primo = False
if primo == True:
    print("El numero es primo")
else:
    print("El numero no es primo")
 