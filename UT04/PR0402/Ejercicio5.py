cadena = input("Ingrese cadena: ")
caracteresVistos = set()
nuevaCadena = ""
for caracter in cadena:
    if caracter not in caracteresVistos:
        nuevaCadena += caracter
        caracteresVistos.add(caracter)
print ("Cadena sin duplicados: ", nuevaCadena)