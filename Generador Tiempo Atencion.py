import aleatorio
import convertidor
import os
import shutil
VAR1=0.031250
VAR2=0.093750
print("\x1b[1;33m"+"La función de probabilidad es una funcion uniforme que oscila entre:")
print("Limite Inferior: ",str(VAR1))
print("Limite Inferior: ",str(VAR2))
CANTP=input("INGRESE LA CANTIDAD DE NUMEROS A GENERAR : ")
CANTP=int(CANTP)
contador=0
archivo = open("GeneradorTiempoAtencion.txt", "w")
archivo.write("Numeros: "+ '\n')
print("Numeros Aleatorios :")
while contador <= CANTP:
    VARIABLE= round(aleatorio.aleatorio(VAR1,VAR2),6)
    contador=contador+1
    print(VARIABLE)
    archivo.write(str(VARIABLE)+ '\n')
print("Los Numeros Fueron Almacenados en el Archivo 'Generador1.txt'")
input("Numeros Generados, Presione Cualquier tecla")
archivo.close()
if os.path.exists("Generdor Atencion"):
    shutil.rmtree('Generdor Atencion')
os.mkdir("Generdor Atencion")
shutil.move("GeneradorTiempoAtencion.txt", "Generdor Atencion")
