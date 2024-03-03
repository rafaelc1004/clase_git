print("\t\tTabla de Multiplicar")

numMul = 0
i = 1
numMul = int(input("Ingrese numero para crear tabla de muliplicar hasta el 10 :"))
    
tabla = []
for x in range(1,11):
    tabla.append(numMul*x)
    
print("\n ")
for x in tabla:
    print(numMul, " * ", i, " = ", x)
    i = i + 1
    
print("\n\t\tFin del programa")