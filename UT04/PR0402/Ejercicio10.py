a = input("Introduce una cadena: ")
sinalpha = ""
for i in a:
    if i.isalpha() == True:
        sinalpha += i
print(sinalpha)