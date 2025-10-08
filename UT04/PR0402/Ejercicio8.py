a = input("Introrduce la primera palabra: ")
b = input("Introduce la segunda palabra: ")
if sorted(a) == sorted(b):
    print("Si, " , a, " y ", b, " son anagramas")
else:
    print("No, " , a, " y ", b, " no son anagramas")