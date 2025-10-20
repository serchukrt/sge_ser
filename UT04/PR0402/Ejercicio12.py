s = input("Introduce una cadena: ")
resultado = []
conteo = 1

for i in range(1, len(s)):
     if s[i] == s[i - 1]:
        conteo += 1
     else:
        resultado.append(s[i - 1] + str(conteo))
        conteo = 1

resultado.append(s[-1] + str(conteo))
print("".join(resultado))