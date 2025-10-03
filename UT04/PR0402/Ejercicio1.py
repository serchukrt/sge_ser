palabra = input("Introduce palabra: ").lower
voc = 0
con = 0
for i in palabra :
    if i in ["a","e","i","o","u"]:
        voc += 1
    else:
        con += 1
print("La palabra tiene")
print(voc, " vocales")
print(con, " consonantes")