import aleatorio
CANTP=input("INGRESE LA CANTIDAD DE NUMEROS A GENERAR : ")
CANTP=int(CANTP)
contador=0
archivo = open("Generador2.txt", "w")
archivo.write("Numeros: "+ '\n')
while contador <= CANTP:
    VARIABLE= aleatorio.aleatorio(0.0031250,0.093750)
    print(VARIABLE)
    contador=contador+1
    archivo.write(str(VARIABLE)+ '\n')
input("Numeros Generados, Presione Cualquier tecla")
archivo.close
