import aleatorio
import convertidor
CANTP=input("INGRESE LA CANTIDAD DE NUMEROS A GENERAR : ")
CANTP=int(CANTP)
contador=0
archivo = open("Generador1.txt", "w")
archivo.write("Numeros: "+ '\n')
print("Numeros Aleatorios :")
while contador <= CANTP:
    VARIABLE= aleatorio.aleatorio(600,1200)
    HORA=convertidor.convertirHora(VARIABLE)
    MINUTOS=convertidor.convertirMinuto(VARIABLE)
    SEGUNDOS=convertidor.convertirSegundo(VARIABLE)
    contador=contador+1
    print(HORA,":",MINUTOS,":",SEGUNDOS)
    archivo.write(str(HORA))
    archivo.write(":")
    archivo.write(str(MINUTOS))
    archivo.write(":")
    archivo.write(str(SEGUNDOS)+ '\n')
print("Los Numeros Fueron Almacenados en el Archivo 'Generador1.txt'")
input("Numeros Generados, Presione Cualquier tecla")
archivo.close()
