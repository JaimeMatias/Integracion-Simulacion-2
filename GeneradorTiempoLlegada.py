import aleatorio
import convertidor
import os
import shutil
VAR1=0.006944
VAR2=0.013889
print("\x1b[1;33m"+"La función de probabilidad es una funcion uniforme que oscila entre:")
print("Limite Inferior: ",str(VAR1))
print("Limite Inferior: ",str(VAR2))
CANTP=input("INGRESE LA CANTIDAD DE NUMEROS A GENERAR : ")
CANTP=int(CANTP)

contador=0
archivo = open("GeneradorTiempoLlegada.txt", "w")
archivo.write("Numeros: "+ '\n')
print("Numeros Aleatorios :")
while contador <= CANTP:
    VARIABLE= round(aleatorio.aleatorio(VAR1,VAR2),6)
    contador=contador+1
    print(VARIABLE)
    archivo.write(str(VARIABLE)+ '\n')
print("Los Numeros Fueron Almacenados en la carpeta 'Generador Llegada'")
print("Los Numeros Fueron Almacenados en el Archivo 'GeneradorTiempoLlegada.txt'")
input("Numeros Generados, Presione Cualquier tecla")
archivo.close()
if os.path.exists("Generdor LLegada"):
    shutil.rmtree('Generdor LLegada')
os.mkdir("Generdor LLegada")
shutil.move("GeneradorTiempoLlegada.txt", "Generador Llegada")
