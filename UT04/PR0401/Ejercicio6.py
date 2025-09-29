cant = int(input("Introduzca cantidad: "))
uniActual = input("Introduzca la cantidad actual: ")
uniDeseada = input("Introduzca unidad deseada: ")
resul = 0

if uniActual == "milimetros" and uniDeseada == "centimetros":
    resul = cant*10
if uniActual == "milimetros" and uniDeseada == "metros":
    resul = cant*1000
if uniActual == "milimetros" and uniDeseada == "kilometros":
    resul = cant*1000000
if uniActual == "centimetros" and uniDeseada == "milimetros":
    resul = cant/10
if uniActual == "centimetros" and uniDeseada == "metros":
    resul = cant*100
if uniActual == "centimetros" and uniDeseada == "kilometros":
    resul = cant*100000
if uniActual == "metros" and uniDeseada == "milimetros":
    resul = cant/1000
if uniActual == "metros" and uniDeseada == "centimetros":
    resul = cant/100
if uniActual == "metros" and uniDeseada == "kilometros":
    resul = cant*1000
if uniActual == "kilometros" and uniDeseada == "milimetros":
    resul = cant/1000000
if uniActual == "kilometros" and uniDeseada == "centimetros":
    resul = cant/100000
if uniActual == "kilometros" and uniDeseada == "metros":
    resul = cant/1000
print(resul)