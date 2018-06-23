import aleatorio
CANTP=input("INGRESE LA CANTIDAD DE PUESTOS DISPONIBLES: ")
CANTP=int(CANTP)
T=0
TPLL=0
TF=39600
TC=[]
for i in range(CANTP):
    TC.append(0)
N=[]
for i in range(CANTP):
    N.append(0)
STP=[]
for i in range(CANTP):
    STP.append(0)
STA=[]
for i in range(CANTP):
    STA.append(0)
STE=[]
for i in range(CANTP):
    STE.append(0)
STO=[]
for i in range(CANTP):
    STO.append(0)
PPS=[]
for i in range(CANTP):
    PPS.append(0)
PTA=[]
for i in range(CANTP):
    PTA.append(0)
PTE=[]
for i in range(CANTP):
    PTE.append(0)
PTO=[]
for i in range(CANTP):
    PTO.append(0)

MIN=MAX=TC[0]
PMIN=PMAX=0
NTC=0
CY=0
CP=0
while T <= TF:
    MIN=MAX=TC[0]
    PMIN=PMAX=0
    T=TPLL
    IA= aleatorio.aleatorio(100,500)
    TPLL=TPLL+IA
    TA= aleatorio.aleatorio(400,800)
    NTC=0
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
    PTE[N4]=STE[N4]/N[N4]
    PTA[N4]=STA[N4]/N[N4]
    PTO[N4]=(STO[N4]/T)*100
    N4=N4+1

print("Promedio de Permanencia: ",PPS)
print("Promedio Tiempo Espera: ",PTE)
print("Promedio Tiempo Atencion: ",PTA)
print("Promedio Tiempo Oscioso: ", PTO)
archivo = open("Resultado.txt", "w")
archivo.write("Promedio de Permanencia: "+ '\n')
for i in PPS:
    VAR10=i
    VAR11=(VAR10//3600)
    VAR12=(VAR10%3600)//60
    archivo.write(str(int(VAR11)))
    archivo.write(":")
    archivo.write(str(int(VAR12)))
    archivo.write(":")
    archivo.write(str(int(VAR10-VAR11*3600-VAR12*60))+ '\n')
archivo.write("Promedio Tiempo Espera: "+ '\n')
for i in PTE:
    VAR10=i
    VAR11=(VAR10//3600)
    VAR12=(VAR10%3600)//60
    archivo.write(str(int(VAR11)))
    archivo.write(":")
    archivo.write(str(int(VAR12)))
    archivo.write(":")
    archivo.write(str(int(VAR10-VAR11*3600-VAR12*60))+ '\n')
archivo.write("Promedio Tiempo Atencion: "+ '\n')
for i in PTA:
    VAR10=i
    VAR11=(VAR10//3600)
    VAR12=(VAR10%3600)//60
    archivo.write(str(int(VAR11)))
    archivo.write(":")
    archivo.write(str(int(VAR12)))
    archivo.write(":")
    archivo.write(str(int(VAR10-VAR11*3600-VAR12*60))+ '\n')
archivo.write("Promedio Tiempo Oscioso: "+ '\n')
for i in PTO:
    VAR10=i
    VAR11=(VAR10//3600)
    VAR12=(VAR10%3600)//60
    archivo.write(str(int(VAR11)))
    archivo.write(":")
    archivo.write(str(int(VAR12)))
    archivo.write(":")
    archivo.write(str(int(VAR10-VAR11*3600-VAR12*60))+ '\n')
archivo.close()
input()
