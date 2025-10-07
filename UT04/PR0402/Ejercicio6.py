a = input("Introduce una cadena: ")
nuevaCadena = ""
for i in a:
    if i == i.upper():
        nuevaCadena += i.lower()
    else:
        nuevaCadena += i.upper()
print (nuevaCadena)