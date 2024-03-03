print("\t Elije un mes del anio")

numMes=0

tuplaAnio = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

while (numMes < 1 or numMes >12):

    print("\n Ingresa el numero del 1 al 12 para saber el mes del anio")
    numMes = int(input("Ingrese el numero del mes :"))
    if (numMes >0 and numMes <=12):
        print("El mes elejido es :", tuplaAnio[numMes-1])
        break
    else:
        print("El numero ingresado no es valido, vuelva a intentarlo")

print("Fin del programa")