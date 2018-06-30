import aleatorio
import convertidor
import mostrar
ciclos=300
CANTP=input("INGRESE LA CANTIDAD DE PUESTOS DISPONIBLES: ")
CANTP=int(CANTP)
archivo = open("Resultado.txt", "w")
archivo2=open("PROMEDIOS"+str(CANTP)+".txt","w")
SPPS=[] #Promedio de Tiempo de Permanencia en cada cola
for i in range(CANTP):
    SPPS.append(0)
SPTA=[]#Promedio de Tiempo de Atencion en cada cola
for i in range(CANTP):
    SPTA.append(0)
SPTE=[] #Promedio de Tiempo de Espera en cada cola
for i in range(CANTP):
    SPTE.append(0)
SPTO=[] #Promedio de Tiempo Oscioso en cada cola
for i in range(CANTP):
    SPTO.append(0)
SPTEX=[]
for i in range(CANTP):
    SPTEX.append(0)

for i in range(ciclos):
    archivo.write("CORRIDA NUMERO: ")
    archivo.write(str(i)+'\n')
    T=0 #Tiempo de la simulacion
    TPLL=0 # Tiempo de la proxima llegada cliente
    TF=39600 # Tiempo Final de la simulacion
    TC=[] # Tiempo Comprometido
    for i in range(CANTP):
        TC.append(0)
    N=[] # Cantidad de Personas en el sistema
    for i in range(CANTP):
        N.append(0)
    STP=[] #Sumatoria de Tiempo de Permanencia en cada cola
    for i in range(CANTP):
        STP.append(0)
    STA=[]#Sumatoria de Tiempo de Atencion en cada cola
    for i in range(CANTP):
        STA.append(0)
    STE=[] #Sumatoria de Tiempo de Espera en cada cola
    for i in range(CANTP):
        STE.append(0)
    STEX=[] #Sumatoria de Tiempo de Exedido en cada cola
    for i in range(CANTP):
        STEX.append(0)
    STO=[] #Sumatoria de Tiempo de oscioso en cada cola
    for i in range(CANTP):
        STO.append(0)
    PPS=[] #Promedio de Tiempo de Permanencia en cada cola
    for i in range(CANTP):
        PPS.append(0)
    PTA=[]#Promedio de Tiempo de Atencion en cada cola
    for i in range(CANTP):
        PTA.append(0)
    PTE=[] #Promedio de Tiempo de Espera en cada cola
    for i in range(CANTP):
        PTE.append(0)
    PTO=[] #Promedio de Tiempo Oscioso en cada cola
    for i in range(CANTP):
        PTO.append(0)
    PTEX=[]
    for i in range(CANTP):
        PTEX.append(0)
    MIN=MAX=TC[0] #Valor minimo y maximo del tiempo Comprometido
    PMIN=PMAX=0 # Posción de la Posicion Minima y Maxima
    NTC=0 # Posicion del vector TC que se está tratando
    CY=0 # Puesto del Lavadero que tienen el menor tiempo Comprometido
    CP=0 # posicion de la distrubicion Ciclica
    while T <= TF:
        MIN=MAX=TC[0]
        PMIN=PMAX=0
        T=TPLL
        IA= aleatorio.aleatorio(600,1200)
        TPLL=TPLL+IA
        TA= aleatorio.aleatorio(2700,8100)
        NTC=0
        #Buscar tiempo Comprometido menor
        for i in TC:
            if MIN >= i:
                MIN=i
                PMIN=NTC
            if  MAX <= i:
                MAX=i
                PMAX=NTC
            NTC=NTC+1
        if MIN != MAX:
            CY=PMIN
        if MIN==MAX:
            CY=CP
            CP=CP+1
            if CANTP ==1:
                CP=0
            if CY==(CANTP+1):
                CP=0


        if T <= TC[CY]:
            STE[CY]=STE[CY]+(TC[CY]-T)
            TC[CY]=TC[CY]+TA
            STA[CY]=STA[CY]+TA
        else:
            STO[CY]=STO[CY]+(T-TC[CY])
            TC[CY]=T+TA
            STA[CY]=STA[CY]+TA
        N[CY]=N[CY]+1
        STP[CY]=STP[CY]+(TC[CY]-T)

    N4=0
    for i in TC:
        PPS[N4]=STP[N4]/N[N4]
        SPPS[N4]=SPPS[N4]+PPS[N4]

        PTE[N4]=STE[N4]/N[N4]
        SPTE[N4]=SPTE[N4]+PTE[N4]

        PTA[N4]=STA[N4]/N[N4]
        SPTA[N4]=SPTA[N4]+PTA[N4]

        PTO[N4]=(STO[N4]/T)*100
        SPTO[N4]=SPTO[N4]+PTO[N4]

        if i>= TF:
            STEX[N4]=(i-39600)
        else:
            STEX[N4]=0

        PTEX[N4]=STEX[N4]
        SPTEX[N4]=SPTEX[N4]+PTEX[N4]
        N4=N4+1
    """
    print("Promedio de Permanencia: ")
    for i in PPS:
        mostrar.mostrar(i)


    print("Promedio Tiempo Espera: ")
    for i in PTE:
        mostrar.mostrar(i)
    print("Promedio Tiempo Atencion: ")
    for i in PTA:
        mostrar.mostrar(i)
    print("Promedio Tiempo Oscioso: ")
    for i in PTO:
        print(round(i,4))

    print("promedio Tiempo de Demora: ")
    for i in PTEX:
        print(round(i,4))
    """
    archivo.write("Promedio de Permanencia: "+ '\n')
    for i in PPS:
        mostrar.imprimir(i,archivo)
    archivo.write("Promedio Tiempo Espera: "+ '\n')
    for i in PTE:
        mostrar.imprimir(i,archivo)
    archivo.write("Promedio Tiempo Atencion: "+ '\n')
    for i in PTA:
        mostrar.imprimir(i,archivo)
    archivo.write("Porcentaje Tiempo Oscioso: "+ '\n')
    for i in PTO:
        archivo.write(str(i)+ '\n')
    archivo.write("Tiempo excedido promedio: "+ '\n')
    for i in PTEX:
        mostrar.imprimir(i,archivo)

archivo.close()

for i in range(CANTP):
    SPPS[i]=SPPS[i]/ciclos
    SPTE[i]=SPTE[i]/ciclos
    SPTA[i]=SPTA[i]/ciclos
    SPTO[i]=SPTO[i]/ciclos
    SPTEX[i]=SPTEX[i]/ciclos



archivo2.write("Promedio de Permanencia: "+ '\n')
for i in SPPS:
    mostrar.imprimir(i,archivo2)
archivo2.write("Promedio Tiempo Espera: "+ '\n')
for i in SPTE:
    mostrar.imprimir(i,archivo2)
archivo2.write("Promedio Tiempo Atencion: "+ '\n')
for i in SPTA:
    mostrar.imprimir(i,archivo2)
archivo2.write("Porcentaje Tiempo Oscioso: "+ '\n')
for i in SPTO:
    archivo2.write(str(round(i,2))+" "+"%"+ '\n')
archivo2.write("Tiempo excedido promedio: "+ '\n')
for i in SPTEX:
    mostrar.imprimir(i,archivo2)
archivo2.close()
print("Los promedios se encuentran Almacenados en el archivo 'PROMEDIOS.TXT'")
print("EL Resultado se encuentra Almacenados en el archivo 'Resultado.txt'")


input()
