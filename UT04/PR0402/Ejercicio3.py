a = input("Introduzca palindromo: ")
limpio = a.replace(" ", "").lower()
if limpio == limpio[::-1]:
    print("Si es un palindromo")
else:
    print("No es un palindromo")