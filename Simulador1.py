import aleatorio
CANTP=input("INGRESE LA CANTIDAD DE NUMEROS A GENERAR : ")
CANTP=int(CANTP)
contador=0
archivo = open("Generador1.txt", "w")
archivo.write("Numeros: "+ '\n')
while contador <= CANTP:
    VARIABLE= aleatorio.aleatorio(0.006944,0.0013889)
    print(VARIABLE)
    contador=contador+1
    archivo.write(str(VARIABLE)+ '\n')
input("Numeros Generados, Presione Cualquier tecla")
archivo.close()
